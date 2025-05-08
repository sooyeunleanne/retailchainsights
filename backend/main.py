from Blockchain import Blockchain
from mainAlgorithm import get_data

blockchain = Blockchain()

# stores data in the blockchain model
def store_data(df):
  for _, row in df.iterrows():
    data = {
      'product': row.get('Products', 'Unknown'),  # default to Unknown if Product not found
      'price': row.get('VALUE', 0),
      'date': row.get('REF_DATE')
    }
    blockchain.add_block(data)

# sample usage
if __name__ == "__main__":
  url = input("Enter URL of the dataset: ")
  df = get_data(url)
  store_data(df)
  # blockchain.print_chain() # prints EVERYTHING, for now
  blockchain.export_chain_to_csv('fetchedData.csv')

