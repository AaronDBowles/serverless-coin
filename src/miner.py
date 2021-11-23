import primitives
import threading
import random

current_transactions = []
current_difficulty = 0
previous_hash = 0

def start():
    sync()
    mine()
def sync():
    threading.Timer(10.0, sync).start()
    # get transactions and difficulty from nodes
    current_transactions = []
    current_difficulty = 0
    previous_hash = 0

def mine():
    # hash until we find a hit
    block = Block(previous_hash,current_transactions)
    if validate_solution(block.hash):
        # submit to the network and keep mining
        submit_block(block)
        mine()
    else:
        # reorder transactions and try again
        current_transactions = random.shuffle(current_transactions)
        mine()

def validate_solution(hash):
    # validate against difficulty parameters
    return True


