import json
import os
from datetime import datetime

def export_retail_price_chain_to_json(blockchain, file_path):
    os.makedirs('fetchedData', exist_ok=True)  # Create directory if it doesn't exist

    data_list = []

    for block in blockchain.chain[1:]:
        raw_date = block.get_date()  # e.g., '2017-01'
        formatted_date = datetime.strptime(raw_date, '%Y-%m').date()  # gives 2017-01-01

        data_list.append({
            "Index": block.index,
            "Timestamp": block.timestamp,
            "Product": block.data['product'],
            "Price": block.data['price'],
            "Date": formatted_date.isoformat(),
            "Previous Hash": block.previous_hash,
            "Hash": block.hash
        })
            
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)

def export_exchange_chain_to_json(blockchain, file_path):
    os.makedirs('fetchedData', exist_ok=True)  # Create directory if it doesn't exist

    data_list = []

    for block in blockchain.chain[1:]:
        raw_date = block.get_date()
        formatted_date = datetime.strptime(raw_date, '%Y-%m').date()
        
        data_list.append({
            "Index": block.index,
            "Timestamp": block.timestamp,
            "Product": block.data['product'],
            "Price": block.data['price'],
            "Date": formatted_date.isoformat(),
            "Previous Hash": block.previous_hash,
            "Hash": block.hash
        })
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)


def export_gdp_chain_to_json(blockchain, file_path):
    os.makedirs('fetchedData', exist_ok=True)  # Create directory if it doesn't exist

    data_list = []

    for block in blockchain.chain[1:]:
        raw_date = block.get_date()
        formatted_date = datetime.strptime(raw_date, '%Y-%m').date()

        data_list.append({
            "Index": block.index,
            "Timestamp": block.timestamp,
            "GDPIndex": block.data['gdp'],
            "Date": formatted_date.isoformat(),
            "Previous Hash": block.previous_hash,
            "Hash": block.hash
        })
        
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)

def export_employment_chain_to_json(blockchain, file_path):
    data_list = []

    for block in blockchain.chain[1:]:
        raw_date = block.get_date()
        formatted_date = datetime.strptime(raw_date, '%Y-%m').date()

        data_list.append({
            "Index": block.index,
            "Timestamp": block.timestamp,
            "Employment": block.data['employment'] * 1000,
            "Date": formatted_date.isoformat(),
            "Previous Hash": block.previous_hash,
            "Hash": block.hash
        })
        
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)