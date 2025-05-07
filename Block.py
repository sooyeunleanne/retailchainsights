import hashlib #provides algo for hashing, such as sha256
import time 
import json

class Block:
    def __init__(self, index, data, previous_hash=''): #constructor
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash #이전 블록 해시
        self.hash = self.calculate_hash() #현재 블록의 고유 해시 값
    
    def calculate_hash(self):
        block_string = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'previous_hash': self.previous_hash
        }, sort_keys = True).encode()

        return hashlib.sha256(block_string).hexdigest()