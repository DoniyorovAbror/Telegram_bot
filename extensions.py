import requests
import json

from config import headers, tickers

class ConvertException(Exception):
    pass

class Covert():

    @staticmethod
    def get_price(_to, _from, _amount):
        if _from not in list(tickers.keys()) or _to not in list(tickers.keys()):
            raise ConvertException("Введён не допустимая валюта\nдопустимые валюты /values")
        elif int(_amount) != 1:
            raise ConvertException("Количество конвертируемых валют должны быть 1")
        elif _to == _from:
            raise ConvertException("Нельзя конвертировать одинаковые валюты")
        else:
            url = f"https://api.apilayer.com/exchangerates_data/convert?to={tickers[_to]}&from={tickers[_from]}&amount={_amount}"
            response = requests.get(url, headers=headers)
            result = json.loads(response.content)
            print(result['result'])
        return result
