import threading
from jsonrpclib.SimpleJSONRPCServer import PooledJSONRPCServer
from jsonrpclib.threadpool import ThreadPool
import sys
import core.sharing

notif_pool = None
request_pool = None
server = None

def start():
    if server is not None and isinstance(server,PooledJSONRPCServer):
        core.sharing.discover_nodes()
        core.sharing.update_node_info(request_pool)

def stop():
    if server is not None and isinstance(server,PooledJSONRPCServer):
        server.server_close()
    sys.exit()

def create_server(host: str, port: int):
    global notif_pool
    global request_pool
    global server
    nofif_pool = ThreadPool(max_threads=10)
    request_pool = ThreadPool(max_threads=10)
    nofif_pool.start()
    request_pool.start()

    server = PooledJSONRPCServer((host, port), 
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
