#https://www.youtube.com/watch?v=iF7osyiDkBY
#API keys
import config
# connection to Alpaca
from alpaca.trading.client import TradingClient

trading_client = TradingClient(config.alpacakey, config.alpacakey_secret)

print(trading_client.get_account().account_number)
print(trading_client.get_account().buying_power)