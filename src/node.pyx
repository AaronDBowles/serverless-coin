import logging
import threading
import core.agent

# most rpc and base protocol code is in the core module
# starting an agent (full_node/miner/executor) 
# will begin the process of syncing data with the rest of the network
server = core.agent.create_server('localhost', 666)
core.agent.start()

# TODO - This agent needs to be responsible for a few different key tasks
# 1. act as a full node, storing and validating the entire chain and all transactions sent to/from this node
# 2. act as a challenger for executors, a necessary part of PoE (Proof-of-Execution)

cdef generate_challenge():
    # TODO - define challenge contract. write first challenges for protocol.
    return {}









