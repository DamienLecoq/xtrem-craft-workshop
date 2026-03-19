from typing import List
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError
from xterm_craft_workshop.money import Money
from xterm_craft_workshop.exchangeRate import ExchangeRate

class Bank:
    _exchange_rate: List[ExchangeRate] = {}
    _pivot_currency: Currency = None

    def __init__(self, exchange_rate = {}, pivot_currency: Currency = None) -> None:
        self._exchange_rate = exchange_rate
        self._pivot_currency = pivot_currency

    @staticmethod
    def create(fromCurrency: Currency, toCurrency: Currency, rate: float) -> "Bank":
        bank = Bank({})
        er = ExchangeRate(rate, from_currency=fromCurrency, to_currency=toCurrency)
        bank.addExchangeRate(er)

        return bank
    
    def addExchangeRate(self, exchange_rate:ExchangeRate) -> None:
        if exchange_rate._from_currency != self._pivot_currency:
            raise ValueError("Must exchange rate from the same currency as the Bank's Pivot Currency")
        self._exchange_rate[f'{exchange_rate._from_currency.value}->{exchange_rate._to_currency.value}'] = exchange_rate._rate

    def convert(self, money: Money, toCurrency: Currency) -> Money:
        from_currency = money.getCurrency()
        amount = money.getMoney()
        if from_currency.value == toCurrency.value:
            return Money(amount, toCurrency)
        key = f'{from_currency.value}->{toCurrency.value}'
        if key not in self._exchange_rate:
            raise MissingExchangeRateError(from_currency, toCurrency)
        rate = self._exchange_rate[key]
        if isinstance(rate, ExchangeRate):
            rate_value = rate._rate
        else:
            rate_value = rate
        return Money(amount * rate_value, toCurrency)