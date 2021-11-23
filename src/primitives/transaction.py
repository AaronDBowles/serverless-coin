class Transaction:
    def __init__(self, signature, transaction_type, details):
        self.signature = signature
        self.type = transaction_type
        self.details = details
        
class TransactionDetails:
    def __init__(self, to_address, amount, target, target_input, target_result, fees):
        self.to_address = to_address
        self.amount = amount
        self.target = target
        self.target_input = target_input
        self.target_result = target_result
        self.fees = fees