from .currency import Currency


class MissingExchangeRateError(Exception):
    def __init__(self, fromCurrency: Currency, toCurrency: Currency) -> None:
        super().__init__(f"There is an exchange error from {fromCurrency.value} to {toCurrency.value}")
