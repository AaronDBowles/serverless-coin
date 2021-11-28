import inspect
import logging
from multiprocessing.pool import ThreadPool
from pathlib import Path
from threading import RLock

from jsonrpclib.SimpleJSONRPCServer import PooledJSONRPCServer

import connection
from src.core import primitives




cdef class Node:
    cdef char* node_type
    cdef char* url
    cdef __init__(self):
        self.node_type = None
        self.url = None

cdef class NodeInfo:
    cdef Node[:] nodes
    cdef primitives.block.Block[:] chain
    cdef primitives.transaction.Transaction[:] executable_transactions
    cdef primitives.transaction.Transaction[:] executed_transactions
    cdef int current_difficult
    cdef primitives.transaction.Block latest_block
    cdef __init__(self):
        self.nodes = []
        self.chain = [] # TODO - add pulling chain from local storage and syncing with server
        self.executable_transactions = []
        self.executed_transactions = []
        self.current_difficulty = 0
        self.latest_block = None

node_info = NodeInfo()
info_lock = RLock()


# called by agent implementations to register any core protocol functions.
# for now, we will try to get away with a model that persists only on pushing node_info updates to each other
cdef register_server_functions(server: PooledJSONRPCServer):
    server.register_function(push_node_info,'push_node_info')

cdef __extract_storage_to_class(storage: str, target: object):
    # for now, we will simply store info as pipe delimited strings
    # TODO - will need to abstract this part into some kind of storage management module
    # since we will be eventually writing to these files more
    line_data = storage.split('|')
    # arbitrarily, well store the attributes in the same order we define them in the class

    # iterate through the attributes of a node and just assign data from line one by one
    for attr in inspect.getmembers(target):
        # could probably write some cool code here to check for valid values based on attr type or something
        target.__setattr__(attr[0], line_data.pop())


# used for initialization of peer nodes
cdef discover_initial_nodes():
    global node_info
    cdef Node[:] new_nodes = []
    # attempt to read cached list of nodes from local storage
    try:

        cdef char* home = str(Path.home())
        with open(f'{home}/serverless-coin/resources/sharing.txt') as file:
            while line := file.readline().rstrip():
                node_update = __extract_storage_to_class(line,Node())
                new_nodes.append(node_update)
    except Exception as error:
        logging.error(error)
    # we also go ahead and add any source nodes
    with open('resources/seed_nodes.txt') as file:
        while line := file.readline().rstrip():
            node_update = __extract_storage_to_class(line, Node())
            new_nodes.append(node_update)
    with info_lock:
        node_info_update = NodeInfo()
        node_info.nodes = new_nodes
        merge_node_info(node_info_update)

cdef add_node(node: Node):
    with info_lock:
        node_info.nodes.append(node)
        logging.info(f'node added to peer list: {node}')

cdef add_executed_transaction(executed_transaction):
    with info_lock:
        node_info.executed_transactions.append(executed_transaction)
        logging.info(f'executed_transaction added to list: {executed_transaction}')

cdef add_executable_transaction(executable_transaction):
    with info_lock:
        node_info.executable_transactions.append(executable_transaction)
        logging.info(f'executable_transaction added to list: {executable_transaction}')

# used by other nodes and executors/miners to push node information to each other
# may be used by new node to tell everyone "Im here!"
# also used by miner to submit blocks
# must be native python function since this is outwardly exposed
def push_node_info(new_node_info):
    with info_lock:
        merge_node_info(new_node_info)

# broadcast our node_info to other nodes, and if we receive node_info in return, merge it
cdef broadcast_node_info_update(pool: ThreadPool):
    results = []
    for node in node_info:
        try:
            logging.info(f'calling get_nodes from: {node}')
            # Enqueue the method
            response = pool.apply_async(connection.run_command,(node.url,"push_node_info",node_info),callback=merge_node_info)
            # Wait for the method to be executed
            logging.info(response)
            results.append(response)
            for r in results:
                r.wait()
        except Exception as error:
            logging.error(error)

# used by threads and anyone else to merge any set of node_info updates into the global node_info
cdef merge_node_info(new_node_info: NodeInfo):
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



