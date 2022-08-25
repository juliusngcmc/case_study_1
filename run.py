from db import sensor_eod_value
from marketstack import get

if __name__ == "__main__":
    ticker_list = ['AAPL', 'C', 'UAL', 'MMM']

    for ticker in ticker_list:
        eod_data = get(ticker)
        sensor_eod_value(
            stock_ticker=eod_data['symbol'],
            eod_date=eod_data['date'],
            open_price=eod_data['open'],
            eod_price=eod_data['close']
        )
