import pytest

from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError
from xterm_craft_workshop.money import Money

@pytest.fixture
def bank() -> Bank:
    return Bank.create(Currency.EUR, Currency.USD, 1.2)


@pytest.fixture
def bank() -> Bank:
    return Bank.create(Currency.EUR, Currency.USD, 1.2)


class TestBank:
    def test_convert_euro_to_usd(self, bank: Bank):
        assert bank.convert(money = Money(10, Currency.EUR), toCurrency = Currency.USD) == 12

    def test_convert_same_currency_returns_same_value(self, bank: Bank):
        assert bank.convert(money = Money(10, Currency.EUR), toCurrency = Currency.EUR) == 10

    def test_convert_with_missing_exchange_rate_throws_exception(self, bank: Bank):
        with pytest.raises(MissingExchangeRateError) as error:
            bank.convert(money = Money(10, Currency.EUR), toCurrency = Currency.KRW)

        assert str(error.value) == "There is an exchange error from EUR to KRW"

    def test_convert_with_different_exchange_rate_returns_different_floats(self, bank: Bank):
        assert bank.convert(money = Money(10, Currency.EUR), toCurrency = Currency.USD) == 12

        bank.addExchangeRate(Currency.EUR, Currency.USD, 1.3)
        assert bank.convert(money = Money(10, Currency.EUR), toCurrency = Currency.USD) == 13
