import core.agent
import logging

# most rpc and base protocol code is in the core module
# starting an agent (full_node/miner/executor) 
# will begin the process of syncing data with the rest of the network
core.agent.create_server('localhost', 667)
core.agent.start()

# Executors exist on the network to execute serverless functions submitted by users 
# this execution data is shared back with other agents  
def execute_transactions():
    # while we have transactions, execute them
    while core.agent.core.sharing.node_info.executable_transactions.count > 0:
        execute_transaction(core.agent.core.sharing.node_info.executable_transactions.pop())
    # when we run out.....try again!
    execute_transactions()

def execute_transaction(transaction):
    logging.info(f'preparing to execute {transaction}')

execute_transactions()
