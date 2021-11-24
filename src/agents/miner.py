import sys
from primitives.block import Block
import threading
import random
import core.sharing
from jsonrpclib.SimpleJSONRPCServer import PooledJsonRpcServer
from multiprocessing.pool import Pool

nofif_pool = Pool()
request_pool = Pool()
nofif_pool.start()
request_pool.start()

server = PooledJSONRPCServer(('localhost', 668), 
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
    core.sharing.discover_nodes()
    mine()

def stop():
    server.stop()
    sys.exit()

def mine():
    # hash until we find a hit
    block = Block(core.sharing.node_info.previous_hash, core.sharing.node_info.executed_transactions)
    if validate_solution(block.hash):
        # submit to the network and keep mining
        submit_block(block)
        mine()
    else:
        # reorder transactions and try again
        core.sharing.node_info.executed_transactions = random.shuffle(core.sharing.node_info.executed_transactions)
        mine()

def validate_solution(hash: str):
    # validate against difficulty parameters
    return True

def submit_block(block: Block):
    # submit hashed block to network
    return True


