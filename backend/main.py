import pandas as pd
from Blockchain import *
from mainAlgorithm import *
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

# Temperature block chaining
temperature_df = pd.read_csv("data/temperature.csv", comment='#')
temperature_df['Date'] = pd.to_datetime(
  temperature_df['Date'].astype(str).str[:4] + '-' + temperature_df['Date'].astype(str).str[4:6],
  errors='coerce'
)
temperature_df = temperature_df[
  (temperature_df['Date'] >= '2017-01-01') &
  (temperature_df['Date'] <= pd.Timestamp.today())
]
temperature_df['Date'] = temperature_df['Date'].dt.strftime('%Y-%m')
temperatureBlockchain = store_temperature(temperature_df)
export_temperature_chain_to_json(temperatureBlockchain, 'fetchedData/temperatureData.json')

# Precipitation block chaining
precipitation_df = pd.read_csv("data/precipitation.csv", comment='#')
precipitation_df['Date'] = pd.to_datetime(
  precipitation_df['Date'].astype(str).str[:4] + '-' + precipitation_df['Date'].astype(str).str[4:6],
  errors='coerce'
)
precipitation_df = precipitation_df[
  (precipitation_df['Date'] >= '2017-01-01') & 
  (precipitation_df['Date'] <= pd.Timestamp.today())
]
precipitation_df['Date'] = precipitation_df['Date'].dt.strftime('%Y-%m')

precipitationBlockchain = store_precipitation(precipitation_df)
export_precipitation_chain_to_json(precipitationBlockchain, 'fetchedData/precipitationData.json')