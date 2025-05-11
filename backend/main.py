from Blockchain import *
from mainAlgorithm import *
import pandas as pd
from chainExportFunctions import *
from helperFunctions import *


#Retail price block chaining
retail_df = get_data("https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810024501")
retailPriceBlockchain = store_data(retail_df)
export_retail_price_chain_to_json(retailPriceBlockchain, 'fetchedData/retailPriceData.json')


#Exchange currency block chaining
exchange_currency_df = get_data("https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3310016301")
exchangeCurrencyBlockchain = store_exchange_data(exchange_currency_df)
export_exchange_chain_to_json(exchangeCurrencyBlockchain, 'fetchedData/exchangeCurrencyData.json')

# GDP block chaining
gdp_df = get_data("https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610010401")
gdpBlockchain = store_gdp_data(gdp_df)
export_gdp_chain_to_json(gdpBlockchain, 'fetchedData/gdpData.json')

#Employment block chaining
employment_df = get_data("https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410037401")
employmentBlockchain = store_employment_data(employment_df)
export_employment_chain_to_json(employmentBlockchain, 'fetchedData/employmentData.json')