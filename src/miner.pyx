from core.primitives.block import Block
import random
import core.agent

# most rpc and base protocol code is in the core module
# starting an agent (full_node/miner/executor) 
# will begin the process of syncing data with the rest of the network
core.agent.create_server('localhost', 667)
core.agent.start()

# miners store a block in memory that represents the block they are actively trying to hash and put transactions into
# this represents a workspace for PoW, NOT a block that has been accepted by the chain
cdef Block block = None

# miners are responsible for taking executed transactions and placing them in blocks 
# for submittal to the network
def mine():
    while 1:
        global block
        if core.agent.sharing.node_info.latest_block.hash != block.previous_hash:
            reset_block_transactions()
        # hash until we find a hit
        if block is None:
            block = Block(core.agent.sharing.node_info.previous_hash, core.agent.sharing.node_info.executed_transactions)
        else:
            block.hash = block.generate_hash()

        if validate_solution(block.hash):
            # submit to the network and keep mining
            submit_block(block)
        else:
            # increment nonce
             block.nonce += 1

cdef reset_block_transactions():
    global block
    # reset the current block workspace, removing any transactions that have been already placed in another block
    

def validate_solution(hash: str):
    # validate against difficulty parameters
    return True

def submit_block(block: Block):
    # submit hashed block to network
    core.agent.core.sharing.node_info.chain.append(block)
    core.agent.core.sharing.node_info.latest_block = block
    core.agent.core.sharing.broadcast_node_info_update(core.agent.request_pool)


mine()