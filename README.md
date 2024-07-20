# TODO

- [x] Create the relevant classes.
- [x] Create the methods for the classes
- [x] Plug a CoinMarketCap API for conversion rates in real-time
- [x] Plug a Stock API (I don't have stocks to list yet)
- [x] Turn the tool to a CLI tool
- [ ] Add a database to store values


## Usage
Add an asset:
```
python main.py add-asset CRYPTO BTC 1.5 64000.0
Crypto - BTC: 1.5 @ 64000.0
```

Update the price of an asset:
```
python main.py update-price BTC 65000.0
Crypto - BTC: 1.5 @ 65000.0
```

Calculate the total value of the portfolio:
```
python main.py calculate-value
Total Portfolio Value in USD: 150042.23452231212
```

List all assets:
```
python main.py list-assets
Crypto - BTC: 1.5 @ 65000.0
```
