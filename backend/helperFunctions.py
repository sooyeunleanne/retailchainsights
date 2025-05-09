from Blockchain import Blockchain
from mainAlgorithm import get_data
from datetime import datetime

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


def cond_date(block, from_date, to_date):
  from_date = datetime.strptime(from_date, "%Y-%m")
  to_date = datetime.strptime(to_date, "%Y-%m")

  block_date_str = str(block.date)
  print("String date: ", {block_date_str})
  
  if not block_date_str:
    print(f"Block is missing a date: {block.date}")
    return False
  
  try:
    block_date = datetime.strptime(block_date_str, "%Y-%m")
  except ValueError:
    print(f"Block has an invalid date format: {block_date_str}")
    return False
  
  return block_date < from_date or block_date > to_date


def cond_product(block, product):
  return block.product == product


# sample usage
if __name__ == "__main__":
  url = input("Enter URL of the dataset: ")
  df = get_data(url)
  store_data(df)

  product = input("Enter product to view: ")
  from_date = input("Enter start date (YYYY-MM): ")
  to_date = input("Enter end date (YYYY-MM): ")

  def condition(block):
    return cond_product(block, product) or cond_date(block, from_date, to_date)

  blockchain.remove_block(condition)
  blockchain.print_chain()
