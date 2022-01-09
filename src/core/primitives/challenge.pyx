from typing import List

from execution import Execution
import uuid

cdef class Challenge:
    cdef str id
    cdef ChallengeTarget target
    executions: List[Execution]
    cdef str transaction_id
    cdef str challenger_signature
    def __init__(self, execution_input: str, target: ChallengeTarget, challenger_signature: str, executions = None):
        self.id = uuid()
        self.target = target
        self.challenger_signature = challenger_signature

cdef class EnvironmentRequirements:
    cdef str operating_system
    cdef str[:] prerequisite_installs


cdef class ChallengeTarget:
    cdef str binary
    cdef str initial_input
    cdef int number_of_executions
    cdef bint feed_outputs_to_next_execution
    cdef EnvironmentRequirements environment_requirements
    def __init__(self, binary: str, initial_input: str, environment_requirements: EnvironmentRequirements = None):
        self.binary = binary
        self.initial_input = initial_input
        self.environment_requirements = environment_requirements
