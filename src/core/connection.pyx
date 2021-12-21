import pyximport; pyximport.install()
import asyncio
from asyncio import new_event_loop
import grpc
import logging
from src.core.protos import full_node_pb2_grpc

LOGGER = logging.getLogger()

asyncio.set_event_loop(new_event_loop())

async def run_command(node_url: str, cmd, params: {}):
    try:
        LOGGER.debug(f'trying to create channel to: {node_url}')
        async with grpc.aio.insecure_channel(node_url) as connection:
            LOGGER.debug(f'connection: {connection}')
            stub = full_node_pb2_grpc.FullNodeStub(connection)
            LOGGER.debug(f'stub activated: {connection}   {stub}')
            future = await stub.push_node_info(params)
            return {'future':future, 'stub':stub}
    except Exception as error:
        raise error
