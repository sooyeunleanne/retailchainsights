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
      'currency': row.get('Type of currency', 'Unknown'),
      'value': row.get('VALUE', 'NaN'),
      'date': row.get('REF_DATE')
    }
    blockchain.add_block(data)
  return blockchain

def store_gdp_data(df):
  blockchain = Blockchain()

  for _, row in df.iterrows():
    if ((row.get('Estimates') == 'Gross domestic product at market prices') and (row.get('COORDINATE') == '1.3.1.30')):
      data = {
        'gdp': row.get('VALUE'),
        'date': row.get('REF_DATE')
      }
      blockchain.add_block(data)

  return blockchain 

def store_employment_data(df):
  blockchain = Blockchain()

  for _, row in df.iterrows():
    if ((row.get('Gender') == 'Total - Gender') and (row.get('Age group') == '15 years and over') and (row.get('COORDINATE') == '1.3.1.1.1')):
      data = {
        'employment': row.get('VALUE'),
        'date': row.get('REF_DATE')
      }
      blockchain.add_block(data)

  return blockchain 

def store_temperature(df):
  blockchain = Blockchain()

  for _, row in df.iterrows():
    data = {
      'date': row.get('Date'),
      'temperature': row.get('Value')
    }
    blockchain.add_block(data)
  return blockchain

def store_precipitation(df):
  blockchain = Blockchain()
  
  for _, row in df.iterrows():
    data = {
      'date': row.get('Date'),
      'precipitation': row.get('Value'),
    }
    blockchain.add_block(data)
  return blockchain


# sample usage
if __name__ == "__main__":
  url = input("Enter URL of the dataset: ")
  df = get_data(url)
  sample = store_gdp_data(df)

  # sample.print_chain()

  