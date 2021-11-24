from typing import List
from flask import Flask
import core.peer_nodes
import connexion
import logging
import requests
import threading

executable_transactions = []
active_executions = []

app = Flask('executor')

def start():
    # initialize node information, kicks off a cycle of continuous node updating
    core.peer_nodes.discover_nodes()
    # TODO - this series of actions can definitely be improved with more intelligent threading
    get_executable_transactions()
    execute_transactions()
    
def execute_transactions():
    # while we have transactions, execute them
    while executable_transactions.count > 0:
        execute_transaction(executable_transactions.pop())
    # when we run out.....try again!
    execute_transactions()

def execute_transaction(transaction):
    logging.info(f'preparing to execute {transaction}')

def get_executable_transactions():
    threading.Timer(30.0, get_executable_transactions).start()
    # query nodes for transactions looking to be included in next block
    for node in core.peer_nodes.nodes:
        try:
            logging.info(f'getting executable transactions from {node}')
            response = requests.get(f'{node}/get_executable_transactions')
            logging.info(response)
            if response.status_code == 200:
                for transaction in response.json()['content']:
                    # get any new transactions or transactions meant to be executed many times
                    if transaction not in executable_transactions or transaction['details']['execution_type'] == 'many':
                        executable_transactions.append(transaction)
        except Exception as error:
            logging.error(error)
    executable_transactions = []
    return True