import hashlib #provides algo for hashing, such as sha256
import time 
import json

class Block:
    def __init__(self, index, product, price, date, previous_hash=''): #constructor
        self.index = index
        self.timestamp = time.time()
        self.product = product
        self.price = price
        self.date = date
        self.previous_hash = previous_hash #이전 블록 해시
        self.hash = self.calculate_hash() #현재 블록의 고유 해시 값
    
    def calculate_hash(self):
        block_string = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'product': self.product,
            'price': self.price,
            'date': self.date,
            'previous_hash': self.previous_hash
        }, sort_keys = True).encode()

        return hashlib.sha256(block_string).hexdigest()
    
    def get_date(self):
        return self.date

#example usage
if __name__ == "__main__":    
    data = {
        'item': '우유',
        'price': 3000,
        'date': '2025-05-06'
    }

    genesis_block = Block(0, data, '0')

    print("📦 Genesis Block Info:")
    print("Index:", genesis_block.index)
    print("Timestamp:", genesis_block.timestamp)
    print("Data:", genesis_block.data)
    print("Previous Hash:", genesis_block.previous_hash)
    print("Current Hash:", genesis_block.hash)