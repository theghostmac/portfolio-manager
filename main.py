from models.portfolio_manager import PortfolioManager
from models.assets import AssetType
import os
from dotenv import load_dotenv

load_dotenv()

CMC_API_KEY = os.getenv('CMC_API_KEY')
if CMC_API_KEY is None:
    raise ValueError("No CMC_API_KEY found. Please set it in the .env file.")

def do_math():
    manager = PortfolioManager(CMC_API_KEY)
    manager.add_asset(AssetType.CRYPTO, "BTC", 1.5, 64000.0)
    manager.add_asset(AssetType.CRYPTO, "USDT", 100, 1.0)
    manager.list_assets()
    print("Total Portfolio Value in USD: ", manager.calculate_portfolio_value())

if __name__ == '__main__':
    do_math()
