import requests
import json
from config import values

class APIException(Exception):
    pass

class CryptoConverter:

    @staticmethod
    def convert(quantity: str, base: str, transferred: str):

        if base == transferred:
            raise APIException(f'Так и останется:{quantity} {base}-{transferred}')

        try:
            base_ticker = values[base]
        except KeyError:
            raise APIException(f'Не найдена валюта {base}')

        try:
            transferred_ticker = values[transferred]
        except KeyError:
            raise APIException(f'Не найдена валюта {transferred}')

        try:
            quantity = float(quantity)
        except ValueError:
            raise APIException(f'Не правильное количество {quantity}')


        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={transferred_ticker}')

        result = json.loads(r.content)[values[transferred]]
        result *= quantity

        return result