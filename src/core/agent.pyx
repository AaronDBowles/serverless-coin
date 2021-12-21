import pyximport; pyximport.install()
from concurrent.futures import ThreadPoolExecutor
import cython
import grpc
from grpc import Server
import sys
from src.core import sharing
from src.core.protos import full_node_pb2_grpc
import logging
LOGGER = logging.getLogger()

cdef class AgentServerInfo:
    cdef public request_pool
    cdef public server
    def __init__(self, server: Server, request_pool: ThreadPoolExecutor):
        self.request_pool = request_pool
        self.server = server


async def start(server_info: AgentServerInfo):
    LOGGER.debug(f'server_info: {server_info.server}')
    if server_info.server is not None and isinstance(server_info.server,grpc.aio.Server):
        LOGGER.info("were starting")
        sharing.start_node_discovery()
        await sharing.broadcast_node_info_update()


def stop(server_info: AgentServerInfo):
    if server_info.server is not None and isinstance(server_info.server,Server):
        server_info.server.stop()
    sys.exit()


async def create_server(host: str, port: int):
    request_pool = ThreadPoolExecutor()
    server = grpc.aio.server(request_pool)
    full_node_pb2_grpc.add_FullNodeServicer_to_server(full_node_pb2_grpc.FullNodeServicer(),server)
    server.add_insecure_port(f'[::]:{port}')
    try:
        await server.start()
        server_info = AgentServerInfo(server,request_pool)
        return server_info
    except Exception as e:
        raise e

