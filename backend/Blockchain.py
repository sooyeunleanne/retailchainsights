from Block import Block 
import csv
import json
from datetime import datetime

class Blockchain:
    def __init__(self):
        self.chain = [] #blockchain list, stores blocks
        self.create_genesis_block() #generate the first block
    
    def create_genesis_block(self): #first block, index 0
        genesis_block = Block(0, 'Genesis Block', 0, 0, 0)
        self.chain.append(genesis_block)
    
    def add_block(self, data): #add a new block
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), data['product'], data['price'], data['date'], previous_block.hash)
        self.chain.append(new_block)
    
    def print_chain(self):
        for block in self.chain:
            print(f'Index: {block.index}')
            print(f'Timestamp: {block.timestamp}') 
            print(f'Product: {block.product}')
            print(f'Price: {block.price}')    
            print(f'Date: {block.date}')                                
            print(f'Previous Hash: {block.previous_hash}')
            print(f'Hash: {block.hash}')
            print('-' * 40)

    def export_chain_to_csv(self, filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Write header
            writer.writerow(['Index', 'Timestamp', 'Product', 'Price', 'Date', 'Previous Hash', 'Hash'])
            
            # Write block data
            for block in self.chain[1:]:
                raw_date = block.get_date()  # e.g., '2017-01'
                formatted_date = datetime.strptime(raw_date, '%Y-%m').date()  # gives 2017-01-01

                writer.writerow([
                    block.index,
                    block.timestamp,
                    block.product,
                    block.price,
                    formatted_date.isoformat(),
                    block.previous_hash,
                    block.hash
                ])
    
    def export_chain_to_json(self, file_path):
        data_list = []

        for block in self.chain[1:]:
            raw_date = block.get_date()  # e.g., '2017-01'
            formatted_date = datetime.strptime(raw_date, '%Y-%m').date()  # gives 2017-01-01

            data_list.append({
                "Index": block.index,
                "Timestamp": block.timestamp,
                "Product": block.product,
                "Price": block.price,
                "Date": formatted_date.isoformat(),
                "Previous Hash": block.previous_hash,
                "Hash": block.hash
            })
                
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data_list, f, ensure_ascii=False, indent=4)


# example usage
if __name__ == "__main__":
    blockchain = Blockchain() #make a blockchain
    # 새 블록 추가
    blockchain.add_block('First block data')
    blockchain.add_block('Second block data')
    blockchain.add_block('Third block data')

    # 블록체인 내용 출력
    blockchain.print_chain()

