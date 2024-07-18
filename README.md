# TODO

- [x] Create the relevant classes.
- [x] Create the methods for the classes
- [x] Plug a CoinMarketCap API for conversion rates in real-time
- [x] Plug a Stock API (I don't have stocks to list yet)
- [x] Turn the tool to a CLI tool
- [ ] Add a database to store values


## Usage

```
python main.py add-asset CRYPTO BTC 1.5 64000.0
# BTC: 1.5 @ 64000.0
```

```
python main.py update-price BTC 65000.0
```

```
python main.py calculate-value
The Total Portfolio Value in USD: 0.0
```

```
python main.py list-assets
```