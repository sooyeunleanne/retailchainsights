from Blockchain import Blockchain
from mainAlgorithm import get_data
from datetime import datetime

# stores data in the blockchain model
def store_data(df):
  blockchain = Blockchain()

  for _, row in df.iterrows():
    data = {
      'product': row.get('Products', 'Unknown'),  # default to Unknown if Product not found
      'price': row.get('VALUE', 0),
      'date': row.get('REF_DATE')
    }
    blockchain.add_block(data)
  return blockchain


def store_exchange_data(df):
  blockchain = Blockchain()

  for _, row in df.iterrows():
    data = {
      'product': row.get('Type of currency', 'Unknown'),
      'price': row.get('VALUE', 'NaN'),
      'date': row.get('REF_DATE')
    }
    blockchain.add_block(data)
  return blockchain



# sample usage
if __name__ == "__main__":
  url = input("Enter URL of the dataset: ")
  df = get_data(url)
  store_data(df)

  blockchain = Blockchain()

  