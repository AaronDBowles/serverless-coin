import sys
from typing import List
import core.sharing
import logging
import requests
import threading
from jsonrpclib.SimpleJSONRPCServer import PooledJSONRPCServer
from multiprocessing.pool import Pool

active_executions = []

nofif_pool = Pool()
request_pool = Pool()
nofif_pool.start()
request_pool.start()

server = PooledJSONRPCServer(('localhost', 667), 
                             thread_pool=request_pool)
server.set_notification_pool(nofif_pool)

server.register_function(lambda x: x, 'ping')
server.register_function(start,"start")
server.register_function(stop,"stop")

# make sure to register your core functions so other nodes can do basic data sharing with you!
core.sharing.register_server_functions(server)

try:
    server.serve_forever()
finally:
    request_pool.stop()
    nofif_pool.stop()
    server.set_notification_pool(None)

def start():
    # initialize node information, kicks off a cycle of continuous node updating
    core.sharing.discover_nodes()
    execute_transactions()

def stop():
    server.stop()
    sys.exit()
    
def execute_transactions():
    # while we have transactions, execute them
    while core.sharing.node_info.executable_transactions.count > 0:
        execute_transaction(core.sharing.node_info.executable_transactions.pop())
    # when we run out.....try again!
    execute_transactions()

def execute_transaction(transaction):
    logging.info(f'preparing to execute {transaction}')
