from Blockchain import *
from mainAlgorithm import get_data
from helperFunctions import *
from chainExportFunctions import *

#Retail price
df = get_data("https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810024501")
retailPriceBlockchain = store_data(df)

currency_df = get_data("https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3310016301")
currencyBlockchain = store_exchange_data(currency_df)

export_retail_price_chain_to_json(retailPriceBlockchain, 'fetchedData/retailPriceChain.json')
export_exchange_chain_to_json(currencyBlockchain, 'fetchedData/exchangePriceChain.json')