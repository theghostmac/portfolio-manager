from models.assets import Asset

class PortolioManager:
    def __init__(self):
        self.assets = []

    def add_asset(self, _symbol: str, _amount: float, _price: float):
        new_asset = Asset(_symbol, _amount, _price)
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
            total_value = asset.amount * asset.price
        return total_value

    def list_assets(self):
        for asset in self.assets:
            print(f"{asset.symbol}: {asset.amount} @ {asset.price}")