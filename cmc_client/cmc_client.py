import requests
import os
from dotenv import load_dotenv

load_dotenv()

CMC_API_KEY=os.getenv('CMC_API_KEY')
if CMC_API_KEY is None:
    raise ValueError("No CMC_API_KEY found. Please set it in the .env file.")

print(CMC_API_KEY)

CMC_PRICE_CONVERSION_URL = "https://pro-api.coinmarketcap.com/v2/tools/price-conversion"

# params: amount & symbol
# response: status & data[]

class CMCClient:
    def __init__(self, api_key):
        self.api_key = api_key
        
    def get_conversion_rate(self, symbol, amount=1):
        params = {
            'symbol': symbol,
            'amount': amount
        }
        
        headers = {
            'X-CMC_PRO_API_KEY': self.api_key
        }
        
        response = requests.get(CMC_PRICE_CONVERSION_URL, params=params, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
            
# Usage example:
cmc_client = CMCClient(CMC_API_KEY)
response = cmc_client.get_conversion_rate('BTC')
print(response)
