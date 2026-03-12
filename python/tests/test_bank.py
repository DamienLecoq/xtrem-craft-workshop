import pytest

from python.src.bank import Bank
from python.src.currency import Currency
from python.src.missing_exchange_rate_error import MissingExchangeRateError


@pytest.fixture
def bank() -> Bank:
    return Bank.create(Currency.EUR, Currency.USD, 1.2)


class TestBank:
    def test_convert_euro_to_usd(self, bank: Bank):
        assert bank.convert(10, Currency.EUR, Currency.USD) == 12

    def test_convert_same_currency_returns_same_value(self, bank: Bank):
        assert bank.convert(10, Currency.EUR, Currency.EUR) == 10

    def test_convert_with_missing_exchange_rate_throws_exception(self, bank: Bank):
        with pytest.raises(MissingExchangeRateError) as error:
            bank.convert(10, Currency.EUR, Currency.KRW)

        assert str(error.value) == "There is an exchange error from EUR to KRW"

    def test_convert_with_different_exchange_rate_returns_different_floats(self, bank: Bank):
        assert bank.convert(10, Currency.EUR, Currency.USD) == 12

        bank.addExchangeRate(Currency.EUR, Currency.USD, 1.3)
        assert bank.convert(10, Currency.EUR, Currency.USD) == 13
