from primitives.block import Block
import random
import core.agent

# most rpc and base protocol code is in the core module
# starting an agent (full_node/miner/executor) 
# will begin the process of syncing data with the rest of the network
core.agent.create_server('localhost', 667)
core.agent.start()

# miners are responsible for taking executed transactions and placing them in blocks 
# for submittal to the network
def mine():
    # hash until we find a hit
    block = Block(core.agent.core.sharing.node_info.previous_hash, core.agent.core.sharing.node_info.executed_transactions)
    if validate_solution(block.hash):
        # submit to the network and keep mining
        submit_block(block)
        mine()
    else:
        # reorder transactions and try again
        core.agent.core.sharing.node_info.executed_transactions = random.shuffle(core.agent.core.sharing.node_info.executed_transactions)
        mine()

def validate_solution(hash: str):
    # validate against difficulty parameters
    return True

def submit_block(block: Block):
    # submit hashed block to network
    return True


