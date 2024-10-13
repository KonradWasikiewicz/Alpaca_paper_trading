#https://www.youtube.com/watch?v=iF7osyiDkBY
#API keys
import config
# connection to Alpaca
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

trading_client = TradingClient(config.alpacakey, config.alpacakey_secret)

market_order_data = MarketOrderRequest(
    symbol="SPY",
    qty= 1,
    side=OrderSide.BUY,
    time_in_force=TimeInForce.DAY
)

market_order=trading_client.submit_order(market_order_data)
print(market_order)

15:30