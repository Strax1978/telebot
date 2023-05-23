import requests
import json
from config import values

class APIException(Exception):
    pass

class CryptoConverter:

    @staticmethod
    def convert(amount: str, base: str, quote: str):

        if base == transferred:
            raise APIException(f'Так и останется:{amount} {base}-{quote}')

        try:
            base_ticker = values[base]
        except KeyError:
            raise APIException(f'Не найдена валюта {base}')

        try:
            transferred_ticker = values[quote]
        except KeyError:
            raise APIException(f'Не найдена валюта {quote}')

        try:
            quantity = float(amount)
        except ValueError:
            raise APIException(f'Не правильное количество {amount}')


        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={transferred_ticker}')

        result = json.loads(r.content)[values[quote]]
        result *= amount

        return result
