import threading

import cython
import logging

from multiprocessing.pool import ThreadPool
from pathlib import Path

import src.core.connection
from jsonrpclib.SimpleJSONRPCServer import PooledJSONRPCServer
from threading import RLock

from src import core
from src.primitives.block import Block
from src.primitives.transaction import Transaction


cdef class Node:
    cdef char* node_type
    cdef char* url
    cdef __init__(self):
        self.node_type = None
        self.url = None

cdef class NodeInfo:
    cdef Node[:] nodes
    cdef Block[:] chain
    cdef Transaction[:] executable_transactions
    cdef Transaction[:] executed_transactions
    cdef int current_difficult
    cdef Block latest_block
    cdef __init__(self):
        self.nodes = []
        self.chain = [] # TODO - add pulling chain from local storage and syncing with server
        self.executable_transactions = []
        self.executed_transactions = []
        self.current_difficulty = 0
        self.latest_block = None

node_info = NodeInfo()
info_lock = RLock()



def register_server_functions(server: PooledJSONRPCServer):
    server.register_function(post_node_info,'post_node_info')
    server.register_function(get_node_info, 'get_node_info')

# used for initialization of peer nodes
def discover_nodes():
    global node_info
    # attempt to read cached list of nodes from local storage
    try:
        new_nodes = []
        home = str(Path.home())
        with open(f'{home}/serverless-coin/resources/sharing.txt') as file:
            while (line := file.readline().rstrip()):
                new_nodes.append(line)
        with info_lock:
            node_info_update = NodeInfo()
            node_info.nodes = new_nodes
            merge_node_info(node_info_update)
    except Exception as error:
        logging.error(error)
    if node_info.nodes.count() is 0:
        # if there is no cache, start from seed file
        with open('resources/seed_nodes.txt') as file:
            while (line := file.readline().rstrip()):
                with info_lock:
                    add_node(line)

def add_node(node_url: str):
    with info_lock:
        node_info.nodes.append(node_url)
        logging.info(f'node added to peer list: {node_url}')

def add_executed_transaction(executed_transaction):
    with info_lock:
        node_info.executed_transactions.append(executed_transaction)
        logging.info(f'executed_transaction added to list: {executed_transaction}')

def add_executable_transaction(executable_transaction):
    with info_lock:
        node_info.executable_transactions.append(executable_transaction)
        logging.info(f'executable_transaction added to list: {executable_transaction}')

# used by other nodes and executors/miners to post node information to each other
# may be used by new node to tell everyone "Im here!"
# also used by miner to submit blocks
def post_node_info(new_node_info):
    with info_lock:
        merge_node_info(new_node_info)

# broadcast our node_info to other nodes, and if we receive node_info in return, merge it
def broadcast_node_info_update(pool: ThreadPool):
    results = []
    for node in node_info:
        try:
            logging.info(f'calling get_nodes from: {node}')
            # Enqueue the method
            response = pool.apply_async(core.connection.run_command,(node,"post_node_info",node_info),callback=merge_node_info)
            # Wait for the method to be executed
            logging.info(response)
            results.append(response)
            for r in results:
                r.wait()
        except Exception as error:
            logging.error(error)

def merge_node_info(new_node_info: NodeInfo):
    if new_node_info.get("nodes", None) is not None:
        for node in  new_node_info.get("nodes"):
            if node not in node_info.nodes:
                add_node(node)
    if new_node_info.get("executable_transactions", None) is not None:
        for transaction in new_node_info.get("executable_transactions"):
            if transaction not in node_info.executable_transactions:
                add_executable_transaction(transaction)
    if new_node_info.get("executed_transactions", None) is not None:
        for transaction in new_node_info.get("executed_transactions"):
            if transaction not in node_info.executed_transactions:
                add_executed_transaction(transaction)

def update_node_info(pool: ThreadPool, node_info:NodeInfo):
    # request peer node updates from everyone in current node list
    current_nodes = node_info.nodes.copy()
    for node in current_nodes:
        try:
            logging.info(f'calling post_node_info from: {node}')
            # Enqueue the method
            response = pool.apply_async(core.connection.run_command(node,"post_node_info"))
            # Wait for the method to be executed
            logging.info(response)
            if response.status_code == 200:
                merge_node_info(response)
        except Exception as error:
            logging.error(error)

# used by other nodes and executors/miners to get info from this node
def get_node_info(include_nodes = True, include_executable_transactions = True, include_executed_transaction = True):
    info = node_info
    if not include_nodes:
        del info.nodes
    if not include_executable_transactions:
        del info.executable_transactions
    if not include_executed_transaction:
        del info.executed_transactions
    return info



