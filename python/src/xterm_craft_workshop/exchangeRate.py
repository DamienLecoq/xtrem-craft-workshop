from typing import Dict
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError
from xterm_craft_workshop.money import Money

class ExchangeRate:
    _rate: float = None
    _from_currency: Currency
    _to_currency: Currency

    def __init__(self, rate: float, from_currency: Currency, to_currency: Currency) -> None:
        if rate < 0 or rate ==None:
            raise ValueError("Negative rate not possible")
        if from_currency == None or to_currency == None:
            raise ValueError("Must give both currencies")
        
        self._rate = rate
        self._from_currency = from_currency
        self._to_currency = to_currency

