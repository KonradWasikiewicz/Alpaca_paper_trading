#https://www.youtube.com/watch?v=iF7osyiDkBY
#API keys
import config
# connection to Alpaca
from alpaca.trading.client import TradingClient

trading_client = TradingClient(config.APCA-API-KEY-ID, config.APCA-API-SECRET-KEY)

print(trading_client.get_account().account_number)
print(trading_client.get_account().buying_power)