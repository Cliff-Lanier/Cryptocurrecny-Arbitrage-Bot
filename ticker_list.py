from kucoin.client import Client
import requests
import json
import pandas as pd


# Define your API key and secret
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'
api_passphrase = 'currencyarbpasscodekjasd;ldfj'

# Define the base URL for the Kucoin API
base_url = 'https://api.kucoin.com'

# Define the endpoint you want to query
endpoint = '/api/v1/market/orderbook/level2_20'

# Define the symbol you want to get the order book for
symbol = 'BTC-USDT'

# Define the headers required for authentication
headers = {
    'Content-Type': 'application/json',
    'KC-API-KEY': api_key,
    'KC-API-PASSPHRASE': api_passphrase
}

# Define the parameters for the request (optional)
params = {
    'symbol': symbol
}

# Send the GET request to the Kucoin API
response = requests.get(base_url + endpoint, headers=headers, params=params)

# Check if the request was successful (HTTP 200 status code)
if response.status_code == 200:
    # Parse the response JSON data
    data = response.json()
    
    # Do something with the data
    print(json.dumps(data, indent=2))  # Print the response data in a formatted way
else:
    # Print the error message if the request was unsuccessful
    print('Error:', response.status_code, response.text)


markets = Client.get_markets()


listcurrencies = Client.get_currencies()
print(listcurrencies[:3])