# Asset represents an asset I own.
class Asset:
    def __init__(self, _symbol, _amount, _price):
        self.symbol = _symbol # e.g. BTC, USDT, ETH
        self.amount = _amount # amount of the asset I own
        self.price = _price # current price of the asset