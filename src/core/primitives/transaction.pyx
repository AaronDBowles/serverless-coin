import uuid

from execution import Execution

cdef class TransactionDetails:
    def __init__(self, to_address: str, amount: float, target: str, target_input: str, fees: float, executions: Execution = None):
        self.to_address = to_address
        self.amount = amount
        self.target = target
        self.target_input = target_input
        self.fees = fees
        self.executions = executions

cdef class Transaction:
    def __init__(self, signature: str, transaction_type: str, details: TransactionDetails):
        self.signature = signature
        self.type = transaction_type
        self.details = details
        self.id = uuid.uuid4()