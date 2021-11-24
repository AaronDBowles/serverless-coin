import threading
from typing import List
from primitives.transaction import Transaction
from jsonrpclib.SimpleJSONRPCServer import PooledJSONRPCServer
from multiprocessing.pool import Pool
import sys
import core.sharing

nofif_pool = Pool()
request_pool = Pool()
nofif_pool.start()
request_pool.start()

server = PooledJSONRPCServer(('localhost', 666), 
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
    sync()

def stop():
    server.stop()
    sys.exit()



def sync():
    threading.Timer(10.0, sync).start()
    validate_chain()

def validate_chain():
    # TODO - grab chain from network and create/validate our copy
    print('chain is valid!')
    return True







