import threading
from typing import List
from primitives.transaction import Transaction
from flask import Flask
import connexion

chain = [] # TODO - add pulling chain from local storage and syncing with server
unexecuted_transactions = []
executed_transactions = []

app = Flask('full-node')
def start_node():
    sync()

def sync():
    threading.Timer(10.0, sync).start()
    validate_chain()

def validate_chain():
    # TODO - grab chain from network and create/validate our copy
    print('chain is valid!')
    return True

# used by a wallet to submit transactions
def post_unexecuted_transactions(transactions):
    current_trans_dict = { trans.id:trans.details in trans for trans in unexecuted_transactions}
    for trans in transactions:
        if current_trans_dict[trans.id] is None:
            unexecuted_transactions.append(trans)


    
# used by an executor to get transactions for execution
def get_executable_transactions():
    # TODO - add logic for multirun transactions
    return unexecuted_transactions

# used by an executor to post executed transactions
def post_executed_transactions(transactions: List[Transaction]):
    executed_transactions.append(transactions)

# used by a miner to get transactions for block creation
def get_executed_transactions():
    return executed_transactions





