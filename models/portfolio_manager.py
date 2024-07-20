from models.assets import Asset, AssetType
from cmc_client.cmc_client import CMCClient
import sqlite3


class PortfolioManager:
    def __init__(self, cmc_api_key, db_name='portfolio.db'):
        self.assets = []
        self.cmc_client = CMCClient(cmc_api_key)
        self.db_conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.db_conn:
            self.db_conn.execute('''
                CREATE TABLE IF NOT EXISTS assets (
                    id INTEGER PRIMARY KEY,
                    asset_type TEXT NOT NULL,
                    symbol TEXT NOT NULL,
                    amount REAL NOT NULL,
                    price REAL NOT NULL
                )
            ''')

    def add_asset(self, _type: AssetType, _symbol: str, _amount: float, _price: float):
        new_asset = Asset(_type, _symbol, _amount, _price)
        self.assets.append(new_asset)
        with self.db_conn:
            self.db_conn.execute('''
                INSERT INTO assets (asset_type, symbol, amount, price)
                VALUES (?, ?, ?, ?)
            ''', (_type.value, _symbol, _amount, _price)
                                 )

    def update_price(self, _symbol: str, _new_price: float):
        with self.db_conn:
            self.db_conn.execute('''
                UPDATE assets SET price = ? WHERE symbol = ?
            ''', (_new_price, _symbol)
                                 )

        # for asset in self.assets:
        #     if asset.symbol == _symbol:
        #         asset.price = _new_price

    def calculate_portfolio_value(self):
        total_value = 0.0
        cursor = self.db_conn.execute('SELECT symbol, amount FROM assets')
        for row in cursor:
            symbol, amount = row
            response = self.cmc_client.get_conversion_rate(symbol, amount)
            if response and 'data' in response:
                for data in response['data']:
                    if data['symbol'] == symbol:
                        usd_price = data['quote']['USD']['price']
                        total_value += amount * usd_price
                        break
        # for asset in self.assets:
        #     response = self.cmc_client.get_conversion_rate(asset.symbol, asset.amount)
        #     if response and 'data' in response:
        #         for data in response['data']:
        #             if data['symbol'] == asset.symbol:
        #                 usd_price = data['quote']['USD']['price']
        #                 total_value += asset.amount * usd_price
        #                 break
        return total_value

    def list_assets(self):
        cursor = self.db_conn.execute('SELECT asset_type, symbol, amount, price FROM assets')
        for row in cursor:
            asset_type, symbol, amount, price = row
            print(f"{asset_type} - {symbol}: {amount} @ {price}")

        # for asset in self.assets:
        #     print(f"{asset.symbol}: {asset.amount} @ {asset.price}")

# Usage example:
# manager = PortfolioManager('your_api_key_here')
# manager.add_asset(AssetType.CRYPTO, "BTC", 1.5, 64000.0)
# manager.add_asset(AssetType.CRYPTO, "USDT", 100, 1.0)
# manager.list_assets()
# print("Total Portfolio Value in USD: ", manager.calculate_portfolio_value())
