# binance-trading-bot
Python Trading Bot for Binance Futures Testnet
## Features

- Market Orders
- Limit Orders
- BUY / SELL support
- CLI interface
- Logging
- Error handling

## Setup

1. Clone repo

2. Install dependencies

pip install -r requirements.txt

3. Create .env

BINANCE_API_KEY=your_key
BINANCE_API_SECRET=your_secret

## Run

Market order:

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit order:

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000

## Logs

Logs are stored in:

logs/bot.log