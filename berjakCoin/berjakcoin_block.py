import hashlib as hasher

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        hash_str = (str(self.index) + 
                   str(self.timestamp) + 
                   str(self.data) + 
                   str(self.previous_hash))\
        # encode the string to bytes after concatenation
        sha.update(hash_str.encode('utf-8'))
        # return the bytes
        return sha.hexdigest()