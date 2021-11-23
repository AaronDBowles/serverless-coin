import block
class Blockchain:
    def __init__(self):
        self.chain = []

    def add_block(self, block):
        self.chain.append(block)
    
    def validate_block(self, block):
        previous_block = self.chain[-1]
        if block.previous_hash != previous_block.getHash():
             return False
        return True
    

