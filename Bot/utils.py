import requests
import json
from config import keys


class ConvertException(Exception):
    pass


class CriptoConverter:

    def __init__(self, text):
        self.text = text

    def command(self):

        value = []
        bases = []
        texts = []

        for num, val in enumerate(self.text.lower().split(' '), start=1):
            if 1 < num <= len(self.text.split(' ')) and val.isalpha():
                bases.append(val)
            else:
                value.append(val)

        try:
            if len(value) < 1 or len(bases) < 1:
                raise ConvertException(f'Некорректная команда, прочитайте справку команда /help ')
        except ConvertException as e:
            return f'Ошибка пользователя \n {e}'

        if len(value) == 1:
            quote = ''.join(value)
            amount = '1'
        else:
            quote, amount = value

        for base in bases:
            try:
                total_base = self.convert(quote, base, amount)
            except ConvertException as e:
                return f'Ошибка пользователя \n {e}'
            except Exception as e:
                return f'Невозможно обработать команду \n {e}'
            else:
                texts.append(f'Цена {amount} {quote.capitalize()} в {base.capitalize()} - {total_base}')

        return '\n'.join(texts)

    def convert(self, quote, base, amount):
        self.quote = quote
        self.base = base
        self.amount = amount

        if self.quote == self.base:
            raise ConvertException(f'Невозможно перевести одинаковые валюты {self.base}')

        try:
            quote_ticker = keys[self.quote]
        except KeyError:
            raise ConvertException(f'Не удалось обработать валюту {self.quote}')

        try:
            base_ticker = keys[self.base]
        except KeyError:
            raise ConvertException(f'Не удалось обработать валюту {self.base}')

        try:
            amounts = float(self.amount)
        except ValueError:
            raise ConvertException(f'Не удалось обработать количество {self.amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')

        total_base = json.loads(r.content)[keys[self.base]] * amounts
        return round(total_base, 4)

    def __str__(self):
        return f'{self.command}'


