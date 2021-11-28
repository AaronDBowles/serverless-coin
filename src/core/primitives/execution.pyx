cdef class Execution:
    cdef __init__(self, transaction_id: str, executor_signature: str, target_hash: str, result_hash: str = None, errors: str = None):
        # to start an execution, we must have a transaction which specifies the details, 
        # as well as a signature of the executor and a hash of the target code to compare against submitted code
        self.transaction_id = transaction_id
        self.executor_signature = executor_signature
        self.target_hash = target_hash
        self.result_hash = result_hash
        self.errors = errors
        