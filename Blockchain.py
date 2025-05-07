from Block import Block 

class Blockchain:
    def __init__(self):
        self.chain = [] #blockchain list, stores blocks
        self.create_genesis_block() #generate the first block
    
    def create_genesis_block(self): #first block, index 0
        genesis_block = Block(0, 'Genesis Block', 0)
        self.chain.append(genesis_block)
    
    def add_block(self, data): #add a new block
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), data, previous_block.hash)
        self.chain.append(new_block)
    
    def print_chain(self):
        for block in self.chain:
            print(f'Index: {block.index}')
            print(f'Timestamp: {block.timestamp}')
            print(f'Data: {block.data}')
            print(f'Previous Hash: {block.previous_hash}')
            print(f'Hash: {block.hash}')
            print('-' * 40)

#example usage
blockchain = Blockchain() #make a blockchain

# 새 블록 추가
blockchain.add_block('First block data')
blockchain.add_block('Second block data')
blockchain.add_block('Third block data')

# 블록체인 내용 출력
blockchain.print_chain()