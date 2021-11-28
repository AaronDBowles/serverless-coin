import hashlib
from cpython.datetime cimport datetime
from transaction import Transaction


cdef class Block:
    cdef char* previous_hash
    cdef Transaction[:] transactions
    cdef datetime creation_time
    cdef int nonce
    cdef char* hash
    def __init__(self, previous_hash, transactions):
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.creation_time = datetime.datetime.now()
        self.nonce = 0
        self.hash = self.generate_hash()


    def generate_hash(self):
        hash = hashlib.sha256()
        hash.update(str(self.previous_hash).encode('utf-8'))
        hash.update(str(self.creation_time).encode('utf-8'))
        hash.update(str(self.transactions).encode('utf-8'))
        hash.update(str(self.nonce).encode('utf-8'))
        return hash.hexdigest()
    
        