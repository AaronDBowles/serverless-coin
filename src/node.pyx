import logging
import random
from multiprocessing import RLock
from core import agent, sharing
from core.primitives.challenge import Challenge, ChallengeTarget, EnvironmentRequirements


# most rpc and base protocol code is in the core module
# starting an agent (full_node/miner/executor) 
# will begin the process of syncing data with the rest of the network
server = agent.create_server('localhost', 666)
node_info = agent.sharing.node_info = sharing.NodeInfo()
info_lock = agent.sharing.info_lock = RLock()
agent.start(server)


# TODO - This agent needs to be responsible for a few different key tasks
# 1. act as a full node, storing and validating the entire chain and all transactions sent to/from this node
# 2. act as a challenger for executors, a necessary part of PoE (Proof-of-Execution)

cdef generate_challenge():
    # TODO - define challenge contract. write first challenges for protocol.
    # the purpose of these challenges by nature requires that ANY code could be used for a challenge
    # this is because actual user created script transactions will also result in challenges that should be indistinguishable
    # from challenges that arent tied to a user created script transaction. We encourage Node developers to implement their
    # own tests, since as long as there is clearly defined output expectations we can use its results to establish good behavior
    # this is fundamental to our proposed Proof-of-Execution consensus protocol when combined with pure function challenges
    # (ie challenges where we can verify execution via a hashing of input + target_binary + output
    # because output is deterministic and can be verified and reproduced by the others). Functions without deterministic output
    # will compare the outputs from all executors to find (or not find) consensus in the results.
    # The results of this entire challenge validation process help dictate an on-chain numeric score
    # that is used to represent good behavior as an executor (influenced heavily by number of successfully completed challenges)
    # a more complete write up of Proof-of-Execution will be added to the README #soon

    # TODO - challenge generation and randomization
    # if we are at an appropriate threshold on the network of validations per executor per block
    # and we have user created executable transactions waiting to be processed
    if agent.sharing.node_info.network_validation_score > agent.sharing.node_info.network_validation_threshold and \
        agent.sharing.node_info.executable_transactions.count() > 0:
        challenge = Challenge()
        challenge_target = ChallengeTarget()
        # we wont actually pop the transaction off the stack until we successfully send it to someone and will be
        # handled by the sharing module or some other module
        transaction = agent.sharing.node_info.executable_transactions[0]
        challenge_target.binary = transaction.details.target
        challenge_target.initial_input = transaction.details.target_input
        challenge.target = challenge_target
        challenge.transaction_id = transaction.id
        return challenge
    # if we have no user transactions, challenge someone
    if agent.sharing.node_info.network_validation_score > agent.sharing.node_info.network_validation_threshold and \
        agent.sharing.node_info.executable_transactions.count() == 0:
        challenge = Challenge()
        challenge_target = ChallengeTarget()
        # a simple test to see if the executor returns the correct element of a given array
        # TODO - build out a module dedicated to randomized challenge generation
        # well just use this for initial testing, though I think it could be a good
        # long term challenge type because of how simple it is
        challenge_target.binary = b'def f(x,y):\n   return x[y]'
        x = []
        i = 0
        # true randomness shouldnt matter for this particular exercise
        while i < random.Random().randint():
            x[i] = random.Random().getrandbits()
            i += i
        y = random.Random().randrange(0,x.count() -1)
        challenge_target.initial_input = {
            'x': x,
            'y': y
        }
        challenge.target = challenge_target
        return challenge









