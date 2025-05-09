from Blockchain import *
from mainAlgorithm import get_data
from chainExportFunctions import *

#Retail price
df = get_data("https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810024501")
retailPriceBlockchain = store_data(df)
# blockchain.print_chain() # prints EVERYTHING, for now
export_retail_price_chain_to_json(retailPriceBlockchain, 'fetchedData/retailPriceData.json')