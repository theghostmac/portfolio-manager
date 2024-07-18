from models.portfolio_manager import PortolioManager

def do_math():
    manager = PortolioManager()
    manager.add_asset("BTC", 1.5, 64_000.0)
    manager.add_asset("USDT", 100, 156_000.0)
    manager.list_assets()
    print("Total Portfolio Value: ", manager.calculate_portfolio_value())

if __name__ == '__main__':
    do_math()
