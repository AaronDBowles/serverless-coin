import json
from pathlib import Path
import logging
import threading
from typing import List
import connection
from jsonrpclib.SimpleJSONRPCServer import PooledJsonRpcServer



class NodeInfo:
    nodes = []
    chain = [] # TODO - add pulling chain from local storage and syncing with server
    executable_transactions = []
    executed_transactions = []
    current_difficulty = 0
    previous_hash = 0
    block_height = 0

node_info = NodeInfo()

def register_server_functions(server: PooledJsonRpcServer):
    server.register_function(post_node_info,'post_node_info')
    server.register_function(get_node_info, 'get_node_info')

# used for initialization of peer nodes
def discover_nodes():
    # attempt to read cached list of nodes from local storage
    try:
        home = str(Path.home())
        with open(f'{home}/serverless-coin/resources/sharing.txt') as file:
            while (line := file.readline().rstrip()):
                add_node(line)
    except Exception as error:
        logging.error(error)
    # if there is no cache, start from seed file
    with open('resources/seed_nodes.txt') as file:
        while (line := file.readline().rstrip()):
            add_node(line)
    update_node_info()

def add_node(node_url: str):
    node_info.nodes.append(node_url)
    logging.info(f'node added to peer list: {node_url}')

def add_executed_transaction(executed_transaction):
    node_info.executed_transactions.append(executed_transaction)
    logging.info(f'executed_transaction added to list: {executed_transaction}')

def add_executable_transaction(executable_transaction):
    node_info.executable_transactions.append(executable_transaction)
    logging.info(f'executable_transaction added to list: {executable_transaction}')

# used by other nodes and executors/miners to post node information to each other
# may be used by new node to tell everyone "Im here!"
def post_node_info(new_node_info):
    merge_node_info(new_node_info)

def merge_node_info(new_node_info):
    if new_node_info.get("nodes", None) is not None:
        for node in  new_node_info.get("nodes"):
            if node not in node_info.nodes:
                add_node(node)
    if new_node_info.get("executable_transactions", None) is not None:
        for transaction in new_node_info.get("executable_transactions"):
            if transaction not in node_info.executable_transactions:
                add_executable_transaction(transaction)
    if new_node_info.get("executed_transactions", None) is not None:
        for transaction in new_node_info.get("executed_transactions"):
            if transaction not in node_info.executed_transactions:
                add_executed_transaction(transaction)

def update_node_info():
    # request peer node updates from everyone in current node list, calls every 10 seconds
    threading.Timer(10.0, update_node_info()).start()
    current_nodes = node_info.nodes.copy()
    for node in current_nodes:
        try:
            logging.info(f'calling get_nodes from: {node}')
            response = connection.run_command(node,"get_node_info")
            logging.info(response)
            if response.status_code == 200:
                merge_node_info(response)
        except Exception as error:
            logging.error(error)

# used by other nodes and executors/miners to get info from this node
def get_node_info(include_nodes = True, include_executable_transactions = True, include_executed_transaction = True):
    info = node_info
    if not include_nodes:
        del info.nodes
    if not include_executable_transactions:
        del info.executable_transactions
    if not include_executed_transaction:
        del info.executed_transactions
    return info



