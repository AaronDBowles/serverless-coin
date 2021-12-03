import pyximport; pyximport.install()
from multiprocessing import RLock

from core import agent, sharing
from core.primitives import challenge
import logging

# most rpc and base protocol code is in the core module
# starting an agent (full_node/miner/executor) 
# will begin the process of syncing data with the rest of the network
from src.core.primitives.execution import Execution

server = agent.create_server('localhost', 667)
node_info = agent.sharing.node_info = sharing.NodeInfo()
info_lock = agent.sharing.info_lock = RLock()
agent.start(server)

# Executors exist on the network to execute serverless functions submitted by users 
# this execution data is shared back with other agents
cdef execute_challenges():
    # while we have transactions, execute them
    # try various multi processing techniques here, may need to rely on data bundled with the execution challenge
    while agent.sharing.node_info.targeted_challenges.count > 0:
        execute_challenge(agent.sharing.node_info.targeted_challenges[0])

cdef execute_challenge(challenge: challenge.Challenge):
    global info_lock
    global node_info
    # using details in execution challenge, spin up a lightweight docker environment with NO outside access (--network none)
    # and execute the binary in the challenge.
    # also need to decide on resource allocation (memory) for the docker container
    logging.info(f'preparing to execute {challenge}')
    try:
        # WARNING: THIS IS UNSAFE AF
        # HURRY AND IMPLEMENT CONTAINERS!!!!!
        result = eval(challenge.target.binary)
        execution = Execution(challenge.id,'mySig',challenge.target.binary,result)
        logging.info(f'result: {result}')
    except Exception as e:
        logging.error(e)
        execution = Execution(challenge.id,'mySig',challenge.target.binary,result)
    if True:
        with info_lock:
            agent.sharing.node_info.targeted_challenges.pop()



execute_challenges()
