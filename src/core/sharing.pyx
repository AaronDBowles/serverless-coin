from concurrent.futures import ThreadPoolExecutor
from typing import List, Any

import pyximport; pyximport.install()
import inspect
import logging
import asyncio
from pathlib import Path
from threading import RLock

import grpc

from src.core import connection
from .primitives import block, transaction, execution, challenge
from src.core.protos import full_node_pb2_grpc, full_node_pb2

LOGGER = logging.getLogger()

cdef enum NodeType:
    FULL_NODE,
    EXECUTOR

class Node:
    url: str
    node_type: NodeType
    def __init__(self, node_type: NodeType = FULL_NODE, url: str = None):
        self.url = url
        self.node_type = node_type


class NodeInfo:
    nodes: List[Node]
    chain: List[block.Block]
    executable_transactions: List[transaction.Transaction]
    executed_transactions: List[transaction.Transaction]
    current_difficulty: int
    network_validation_score: float
    network_validation_threshold: float
    latest_block: block.Block
    unverified_challenges: List[challenge.Challenge]
    unverified_executions: List[execution.Execution]
    targeted_challenges: List[challenge.Challenge]
    def __init__(self):
        self.nodes = []
        self.chain = [] # TODO - add pulling chain from local storage and syncing with server
        self.executable_transactions = []
        self.executed_transactions = []
        self.current_difficulty = 0
        self.latest_block = None
        self.network_validation_score = 0
        self.network_validation_threshold = 0

# global state, initiated by implementing agent, updated here
node_info: NodeInfo
info_lock: RLock


cdef __extract_storage_to_class(storage: str, target: object):
    # for now, we will simply store info as pipe delimited strings
    # TODO - will need to abstract this part into some kind of storage management module
    # since we will be eventually writing to these files more
    line_data = storage.split('|')
    # arbitrarily, well store the attributes in the same order we define them in the class
    LOGGER.debug(f'about to transform {line_data} into {target.__str__()}')
    # iterate through the attributes of a node and just assign data from line one by one
    LOGGER.debug(f'vars {vars(target)}')
    for attr in vars(target):
        LOGGER.debug(f'attr: {attr}')
        # could probably write some cool code here to check for valid values based on attr type or something
        target.__setattr__(attr, line_data.pop(0))
    return target


# used for initialization of peer nodes
def start_node_discovery():
    global  info_lock
    cdef new_nodes = []
    # attempt to read cached list of nodes from local storage
    try:
        # TODO - make this copy the files to the users folders if they dont exist, then read from there opposed to src
        home = str(Path.home())
        with open(f'C:/sandbox/serverless-coin/src/resources/sharing.txt') as file:
            line = file.readline().rstrip()
            while line:
                node_update = __extract_storage_to_class(line,Node())
                new_nodes.append(node_update)
                line = file.readline().rstrip()

        # we also go ahead and add any source nodes
        with open(f'C:/sandbox/serverless-coin/src/resources/seed_nodes.txt') as file:
            line = file.readline().rstrip()
            while line:
                node_update = __extract_storage_to_class(line, Node())
                new_nodes.append(node_update)
                line = file.readline().rstrip()
        with info_lock:
            node_info_update = NodeInfo()
            node_info.nodes = new_nodes
            LOGGER.debug(f'about to merge seed nodes: {node_info_update.nodes}')
            merge_node_info(node_info_update)
    except Exception as error:
        LOGGER.error(error)

cdef add_node(node: Node):
    with info_lock:
        node_info.nodes.append(node)
        LOGGER.info(f'node added to peer list: {node}')

cdef add_executed_transaction(executed_transaction):
    with info_lock:
        node_info.executed_transactions.append(executed_transaction)
        LOGGER.info(f'executed_transaction added to list: {executed_transaction}')

cdef add_executable_transaction(executable_transaction):
    with info_lock:
        node_info.executable_transactions.append(executable_transaction)
        LOGGER.info(f'executable_transaction added to list: {executable_transaction}')

# used by other nodes and executors/miners to push node information to each other
# may be used by new node to tell everyone "Im here!"
# also used by miner to submit blocks
# must be native python function since this is outwardly exposed
def push_node_info(new_node_info, context):
    LOGGER.info(f'received: {new_node_info} with {context}')
    with info_lock:
        merge_node_info(new_node_info)

def push_challenge(challenge, context):
    global node_info
    LOGGER.info(f'received: {challenge} with {context}')
    with info_lock:
        node_info.targeted_challenges.append(challenge)


def map_node_info_to_message(node_info: NodeInfo):
    message = full_node_pb2.NodeInfo()
    for node in node_info.nodes:
        message_node = full_node_pb2.Node()
        message_node.node_type = node.node_type.__str__()
        message_node.url = node.url
        message.nodes.append(message_node)
    return message

def send_targeted_challenge(challenge: challenge.Challenge):
    with grpc.aio.insecure_channel('localhost:667') as channel:
        stub = full_node_pb2_grpc.FullNodeStub(channel)
        logging.info(f'sending challenge {challenge}')
        stub.push_challenge(challenge)


# broadcast our node_info to other nodes, and if we receive node_info in return, merge it
async def broadcast_node_info_update():
    results = []
    LOGGER.debug(f'nodes: {node_info.nodes}')
    for node in node_info.nodes:
        try:
            LOGGER.info(f'calling get_nodes from: {node}')
            response = await connection.run_command(node.url,full_node_pb2_grpc.FullNode.push_node_info,map_node_info_to_message(node_info))
            LOGGER.debug(f'response: {response}')
            asyncio.create_task(future_result_merge_node_info(response["future"]))
            # Wait for the method to be executed
            LOGGER.info(response)
        except Exception as error:
            LOGGER.error(error)
    return node_info

async def future_result_merge_node_info(future):
    merge_node_info(await future)

# used by threads and anyone else to merge any set of node_info updates into the global node_info
cdef merge_node_info(new_node_info: Any):
    LOGGER.debug(f'merging node info: {new_node_info}')
    with info_lock:
        if new_node_info.nodes is not None:
            for node in new_node_info.nodes:
                if node not in node_info.nodes:
                    add_node(node)
        if new_node_info.executable_transactions is not None:
            for transaction in new_node_info.executable_transactions:
                if transaction not in node_info.executable_transactions:
                    add_executable_transaction(transaction)
        if new_node_info.executed_transactions is not None:
            for transaction in new_node_info.executed_transactions:
                if transaction not in node_info.executed_transactions:
                    add_executed_transaction(transaction)

# Not going to even bother fixing this for now, would like to explore a completely push based model
# for speed of notification of updates
# def update_node_info(pool: ThreadPool, node_info:NodeInfo):
#     # request peer node updates from everyone in current node list
#     for node in current_nodes:
#         try:
#             logging.info(f'calling push_node_info from: {node}')
#             # Enqueue the method
#             response = pool.apply_async(core.connection.run_command(node,"push_node_info"))
#             # Wait for the method to be executed
#             logging.info(response)
#             if response.status_code == 200:
#                 merge_node_info(response)
#         except Exception as error:
#             logging.error(error)

# like the above function, commenting this out for now,
# since well try only pushes for now until we find a reason to use pull
# # used by other nodes and executors/miners to get info from this node
# def get_node_info(include_nodes = True, include_executable_transactions = True, include_executed_transaction = True):
#     info = node_info
#     if not include_nodes:
#         del info.nodes
#     if not include_executable_transactions:
#         del info.executable_transactions
#     if not include_executed_transaction:
#         del info.executed_transactions
#     return info



