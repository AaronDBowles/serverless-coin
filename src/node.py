import threading
import primitives

chain = [] # TODO - add pulling chain from local storage and syncing with server
unprocessed_transactions = []

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
def post_unprocessed_transaction(transactions):
    current_trans_dict = { trans.id:trans.details in trans for trans in unprocessed_transactions}
    for trans in transactions:
        if current_trans_dict[trans.id] is None:
            unprocessed_transactions.append(trans)


    
# used by a miner to get transactions for block creation
def get_unprocessed_transaction():
    return unprocessed_transactions




