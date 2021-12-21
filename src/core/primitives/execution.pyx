cdef class Execution:
    def __init__(self, challenge_id: str, executor_signature: str, target_hash: str, result_hash: str = None, errors: str = None):
        # to start an execution, we must have a challenge which specifies the details,
        # as well as a signature of the executor and a hash of the target code to compare against submitted code
        self.challenge_id = challenge_id
        self.executor_signature = executor_signature
        self.target_hash = target_hash
        self.result_hash = result_hash
        self.errors = errors
        