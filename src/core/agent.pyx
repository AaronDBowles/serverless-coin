import pyximport; pyximport.install()
from concurrent.futures import ThreadPoolExecutor

import grpc
from grpc import Server
import sys
import sharing
from src.core.protos import full_node_pb2_grpc

cdef class AgentServerInfo:
    request_pool = None
    server = None
    def __init__(self, server: Server, request_pool: ThreadPoolExecutor):
        self.request_pool = request_pool
        self.server = server

cdef start(server_info: AgentServerInfo):
    if server_info.server is not None and isinstance(server_info.server,Server):
        sharing.start_node_discovery()
        sharing.broadcast_node_info_update(server_info.request_pool)

cdef stop(server_info: AgentServerInfo):
    if server_info.server is not None and isinstance(server_info.server,Server):
        server_info.server.stop()
    sys.exit()

def create_server(host: str, port: int):
    request_pool = ThreadPoolExecutor()
    server = grpc.aio.server(request_pool)
    full_node_pb2_grpc.add_FullNodeServicer_to_server(full_node_pb2_grpc.FullNodeServicer(),server)
    server.add_insecure_port(f'[::]:{port}')
    try:
        server.start()
        server_info = AgentServerInfo(server,request_pool)
        server.wait_for_termination()
        return server_info
    finally:
        server.stop()

