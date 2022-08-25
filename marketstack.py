import requests
from config import MS_ACCESS_KEY


def get(stock_ticker):
    params = {
        'access_key': MS_ACCESS_KEY
    }
    url = 'http://api.marketstack.com/v1/tickers/{0}/eod/latest'.format(stock_ticker)
    results = requests.get(url, params=params)
    return results.json()


class EndOfDayAPI:
    pass


class RealTimeAPI:
    def get(self):
        pass
