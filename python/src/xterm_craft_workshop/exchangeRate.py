from typing import Dict
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError
from xterm_craft_workshop.money import Money

class ExchangeRate:
    _rate: float = None
    _from_currency: Currency = None
    _to_currency: Currency = None

    def __init__(self, rate: float = None, from_currency: Currency = None, to_currency: Currency = None) -> None:
        self._rate = rate
        self._from_currency = from_currency
        self._to_currency = to_currency

    @staticmethod
    def create(fromCurrency: Currency, toCurrency: Currency, rate: float) -> "ExchangeRate":
        ExchangeRate = ExchangeRate({})
        ExchangeRate.addExchangeRate(fromCurrency, toCurrency, rate)

        return ExchangeRate
    
    def addExchangeRate(self, fromCurrency: Currency, toCurrency: Currency, rate: float) -> None:
        self._exchange_rate[f'{fromCurrency.value}->{toCurrency.value}'] = rate

    def convert(self, money: Money, toCurrency: Currency) -> float:
        fromCurrency = money.getCurrency()
        amount = money.getMoney()
        if not (fromCurrency.value == toCurrency.value or f'{fromCurrency.value}->{toCurrency.value}' in self._exchange_rate):
            raise MissingExchangeRateError(fromCurrency, toCurrency)
        return Money(amount, toCurrency) if fromCurrency.value == toCurrency.value  else Money(amount * self._exchange_rate[f'{fromCurrency.value}->{toCurrency.value}'], toCurrency)