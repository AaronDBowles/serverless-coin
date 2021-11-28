from jsonrpclib.SimpleJSONRPCServer import PooledJSONRPCServer
from jsonrpclib.threadpool import ThreadPool
import sys
import core.sharing



def AgentServerInfo(server: PooledJSONRPCServer, notif_pool: ThreadPool, request_pool: ThreadPool):
    notif_pool = None
    request_pool = None
    server = None

def start(server_info: AgentServerInfo):
    if server_info.server is not None and isinstance(server_info.server,PooledJSONRPCServer):
        core.sharing.discover_nodes()
        core.sharing.update_node_info(server_info.request_pool)

def stop(server_info: AgentServerInfo):
    if server_info.server is not None and isinstance(server_info.server,PooledJSONRPCServer):
        server_info.server.server_close()
    sys.exit()

def create_server(host: str, port: int):
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
        server_info = AgentServerInfo(server,nofif_pool,request_pool)
        return server_info
    finally:
        request_pool.stop()
        nofif_pool.stop()
        server.set_notification_pool(None)
