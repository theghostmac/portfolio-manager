from models.assets import Asset
from cmc_client.cmc_client import CMCClient

class PortolioManager:
    def __init__(self, cmc_api_key):
        self.assets = []
        self.cmc_client = CMCClient(cmc_api_key)

    def add_asset(self, _type: str, _symbol: str, _amount: float, _price: float):
        new_asset = Asset(_type, _symbol, _amount, _price)
        self.assets.append(new_asset)

    # plug a coinmarketcap API to fetch the real price of crypto assets.
    # plug a stocks API to fetch the real price of stock assets.
    def update_price(self, _symbol: str, _new_price: float):
        for asset in self.assets:
            if asset.symbol == _symbol:
                asset.price = _new_price

    def calculate_portfolio_value(self):
        total_value = 0.0
        for asset in self.assets:
            response = self.cmc_client.get_conversion_rate(asset.symbol, asset.amount)
            if response and 'data' in response:
                usd_price = response['data']['quote']['USD']['price']
                total_value += asset.amount * usd_price
        return total_value

    def list_assets(self):
        for asset in self.assets:
            print(f"{asset.symbol}: {asset.amount} @ {asset.price}")
            

# Usage example:
manager = PortolioManager('17b34b50-703b-4a3b-8d48-c87cc4d7a144')
manager.add_asset("Crypto", "BTC", 1.5, 64000.0)
manager.add_asset("Crypto", "USDT", 100, 1.0)
manager.list_assets()
print("Total Portfolio Value in USD: ", manager.calculate_portfolio_value())