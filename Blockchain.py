from Block import Block 

class Blockchain:
    def __init__(self):
        self.chain = [] #blockchain list, stores blocks
        self.create_genesis_block() #generate the first block
    
    def create_genesis_block(self): #first block, index 0
        genesis_block = Block(0, 'Genesis Block', 0)
        self.chain.append(genesis_block)
