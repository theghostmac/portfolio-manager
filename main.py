import click
from models.portfolio_manager import PortfolioManager
from models.assets import AssetType
import os
from dotenv import load_dotenv

load_dotenv()

CMC_API_KEY = os.getenv('CMC_API_KEY')
if CMC_API_KEY is None:
    raise ValueError("No CMC_API_KEY found. Please set it in the .env file.")

@click.group()
def cli():
    """A CLI Tool to manage your assets portfolio"""
    pass

@cli.command()
@click.argument('type')
@click.argument('symbol')
@click.argument('amount', type=float)
@click.argument('price', type=float)
def add_asset(type, symbol, amount, price):
    '''Add an asset to your portfolio'''
    manager = PortfolioManager(CMC_API_KEY)
    asset_type = AssetType[type.upper()]
    manager.add_asset(asset_type, symbol, amount, price)
    manager.list_assets()
    
@cli.command()
@click.argument('symbol')
@click.argument('new_price', type=float)
def update_price(symbol, new_price):
    """Update the price of an asset in your portfolio"""
    manager = PortfolioManager(CMC_API_KEY)
    manager.update_price(symbol, new_price)
    manager.list_assets()
    

@cli.command()
def calculate_value():
    """Calculaes the total value of your portfolio"""
    manager = PortfolioManager(CMC_API_KEY)
    total_value = manager.calculate_portfolio_value()
    click.echo(f"The Total Portfolio Value in USD: {total_value}")
    

@cli.command()
def list_assets():
    """List all assets in your portfolio"""
    manager = PortfolioManager(CMC_API_KEY)
    manager.list_assets()
    
    
if __name__ == '__main__':
    cli()