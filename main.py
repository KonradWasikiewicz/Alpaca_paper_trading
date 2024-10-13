# #https://www.youtube.com/watch?v=iF7osyiDkBY
# #API keys
# import config
# # connection to Alpaca
# from alpaca.trading.client import TradingClient

# trading_client = TradingClient(config.alpacakey, config.alpacakey_secret)

# print(trading_client.get_account().account_number)
# print(trading_client.get_account().buying_power)


from alpaca.data import StockHistoricalDataClient, StockTradesRequest
from datetime import datetime

data_client = StockHistoricalDataClient("PKQGC4V9XTMJGSD9HF29","2HRWei8pngjyCJmQeceFowiarg6Ktrd2zG9wQ0Qt")

request_params = StockTradesRequest(
    symbol_or_symbols = "PLTR",
    start = datetime(2024, 1, 30, 14, 30),
    end = datetime(2024, 1, 30, 14, 45) 
)

trades = data_client.get_stock_trades(request_params)

for trades in trades.data['PLTR']:
    print(trades)
    break

11 minuta