from typing import Dict
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError


class Bank:
    _exchange_rate: Dict[str, float] = {}

    def __init__(self, exchange_rate = {}) -> None:
        self._exchange_rate = exchange_rate

    @staticmethod
    def create(fromCurrency: Currency, toCurrency: Currency, rate: float) -> "Bank":
        bank = Bank({})
        bank.addExchangeRate(fromCurrency, toCurrency, rate)

        return bank
    
    def addExchangeRate(self, fromCurrency: Currency, toCurrency: Currency, rate: float) -> None:
        self._exchange_rate[f'{fromCurrency.value}->{toCurrency.value}'] = rate

    def convert(self, amount: float, fromCurrency: Currency, toCurrency: Currency) -> float:
        if not (fromCurrency.value == toCurrency.value or f'{fromCurrency.value}->{toCurrency.value}' in self._exchange_rate):
            raise MissingExchangeRateError(fromCurrency, toCurrency)
        return amount if fromCurrency.value == toCurrency.value  else amount * self._exchange_rate[f'{fromCurrency.value}->{toCurrency.value}']