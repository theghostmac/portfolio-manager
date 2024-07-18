from enum import Enum

# enums for asset types
class AssetType(Enum):
    CRYPTO = 'Crypto'
    STOCK = 'Stock'
    REAL_ESTATE = 'Real Estate'
    BOND = 'Bond'
    COMMODITY = 'Commodity'
    OTHER = 'Other'

# Asset represents an asset I own.
class Asset:
    def __init__(self, _type: AssetType, _symbol: str, _amount: float, _price: float):
        if not isinstance(_type, AssetType):
            raise ValueError(f"Invalid asset type: {_type}. Must be an instance of AssetType Enum.")
        
        self.type = _type # whether the asset is a Crypto asset or a Stock asset, etc.
        self.symbol = _symbol # e.g. BTC, USDT, ETH
        self.amount = _amount # amount of the asset I own
        self.price = _price # current price of the asset
        
    def __str__(self) -> str:
        return f"{self.type.value} - {self.symbol}: {self.amount} @ {self.price}"
    
    def __repr__(self) -> str:
        return f"Asset(type={self.type}, symbol={self.symbol}, amount={self.amount}, price={self.price})"