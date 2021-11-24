from pathlib import Path
import logging
from typing import List
import requests
import threading

nodes = []

# used for initialization of peer nodes
def discover_nodes():
    # attempt to read cached list of nodes from local storage
    try:
        home = str(Path.home())
        with open(f'{home}/serverless-coin/resources/peer_nodes.txt') as file:
            while (line := file.readline().rstrip()):
                add_node(line)
    except Exception as error:
        logging.error(error)
    # if there is no cache, start from seed file
    with open('resources/seed_nodes.txt') as file:
        while (line := file.readline().rstrip()):
            add_node(line)
    request_nodes()

def add_node(node_url: str):
    nodes.append(node_url)
    logging.info(f'node added to peer list: {node_url}')

# used by other nodes and executors/miners to post node information to each other
# may be used by new node to tell everyone "Im here!"
def post_nodes(new_nodes: List[str]):
    for node in new_nodes:
        if node not in nodes:
            add_node(node)

def request_nodes():
    # request peer node updates from everyone in current node list, calls every 10 mins
    threading.Timer(600.0, request_nodes()).start()
    current_nodes = nodes.copy()
    for node in current_nodes:
        try:
            logging.info(f'calling get_nodes from: {node}')
            response = requests.get(f'{node}/get_nodes')
            logging.info(response)
            if response.status_code == 200:
                for new_node in response.content:
                    if new_node not in nodes:
                        add_node(new_node)
        except Exception as error:
            logging.error(error)

#used by other nodes and executors/miners to get the node list from this node
def get_nodes():
    return nodes

