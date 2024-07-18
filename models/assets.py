from enum import Enum

# create enums: Crypto, Stock, what else?

# Asset represents an asset I own.
class Asset:
    def __init__(self, _type, _symbol, _amount, _price):
        self.type = _type # whether the asset is a Crypto asset or a Stock asset, etc.
        self.symbol = _symbol # e.g. BTC, USDT, ETH
        self.amount = _amount # amount of the asset I own
        self.price = _price # current price of the asset