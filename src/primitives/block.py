import hashlib
import jsonify
import json
import datetime
import transaction

class Block:
    def __init__(self, previous_hash, transactions):
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.creation_time = datetime.datetime.now()
        self.hash = self.getHash()


    def getHash(self):
        hash = sha256()
        hash.update(str(self.previous_hash).encode('utf-8'))
        hash.update(str(self.creation_time).encode('utf-8'))
        hash.update(str(self.transactions).encode('utf-8'))
        return hash.hexdigest()
    
        
