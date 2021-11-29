import core.agent
import logging

# most rpc and base protocol code is in the core module
# starting an agent (full_node/miner/executor) 
# will begin the process of syncing data with the rest of the network
core.agent.create_server('localhost', 667)
core.agent.start()

# Executors exist on the network to execute serverless functions submitted by users 
# this execution data is shared back with other agents  
cdef execute_transactions():
    # while we have transactions, execute them
    # try various multi processing techniques here, may need to rely on data bundled with the execution challenge
    while core.agent.sharing.node_info.executable_transactions.count > 0:
        execute_transaction(core.agent.sharing.node_info.executable_transactions.pop())

cdef execute_transaction(transaction):
    # using details in execution challenge, spin up a lightweight docker environment with NO outside access (--network none)
    # and execute the binary in the challenge.
    # also need to decide on resource allocation (memory) for the docker container
    logging.info(f'preparing to execute {transaction}')

execute_transactions()
