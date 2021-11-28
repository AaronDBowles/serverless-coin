import uuid
import random
import hashlib
from primitives.transaction import Transaction, TransactionDetails
import wallet
import threading
import json

def run_timed_transactions():
    threading.Timer(15,run_timed_transactions).start()
    transaction = generate_transaction()
    print(f'pushing transaction {transaction}')
    wallet.push_transaction_to_network(transaction)


def generate_transaction_details():
    to_address = uuid.uuid4()
    target = 'test_target.py'
    target_input = "{'name'='Aaron'}"
    amount = random.random()
    fees = amount * 0.001
    details = TransactionDetails(to_address,amount,target,target_input,fees)
    return details

def generate_transaction():
    id = uuid.uuid4()
    type = "P2P"
    details = generate_transaction_details()
    signature = hashlib.sha256(str("Aaron Is the best").encode('utf-8')).hexdigest()
    transaction = Transaction(signature,type,details)
    return transaction

run_timed_transactions()

