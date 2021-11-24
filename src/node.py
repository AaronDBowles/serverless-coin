import logging
import threading
import core.agent

# most rpc and base protocol code is in the core module
# starting an agent (full_node/miner/executor) 
# will begin the process of syncing data with the rest of the network
core.agent.create_server('localhost', 666)
core.agent.start()

# full_nodes also have the added responsibility of storing and validating the chain
def sync():
    threading.Timer(10.0, sync).start()
    validate_chain()

def validate_chain():
    # TODO - grab chain from network and create/validate our copy
    logging.info(f'chain is valid! {core.agent.core.sharing.node_info.chain}')
    return True

sync()






