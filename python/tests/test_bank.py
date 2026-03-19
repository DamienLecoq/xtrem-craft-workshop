import pytest

from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError
from xterm_craft_workshop.money import Money
from xterm_craft_workshop.bankBuilder import CreateBankBuilder
from xterm_craft_workshop.exchangeRate import ExchangeRate

@pytest.fixture
def bank() -> Bank:
    return CreateBankBuilder().ABank().WithExchangeRate(Currency.EUR, Currency.USD,1.2).WithPivotCurrency(Currency.EUR).build()

class TestBank:
    def test_convert_euro_to_usd(self, bank: Bank):
        assert bank.convert(money = Money(10, Currency.EUR), toCurrency = Currency.USD) == Money(12, Currency.USD)

    def test_convert_same_currency_returns_same_value(self, bank: Bank):
        assert bank.convert(money = Money(10, Currency.EUR), toCurrency = Currency.EUR) == Money(10, Currency.EUR)

    def test_convert_with_missing_exchange_rate_throws_exception(self, bank: Bank):
        with pytest.raises(MissingExchangeRateError) as error:
            bank.convert(money = Money(10, Currency.EUR), toCurrency = Currency.KRW)

        assert str(error.value) == "There is an exchange error from EUR to KRW"

    def test_convert_with_different_exchange_rate_returns_different_floats(self, bank: Bank):
        assert bank.convert(money = Money(10, Currency.EUR), toCurrency = Currency.USD) == Money(12, Currency.USD)
        er = ExchangeRate( 1.3, Currency.EUR, Currency.USD)
        bank.addExchangeRate(er)
        assert bank.convert(money = Money(10, Currency.EUR), toCurrency = Currency.USD) == Money(13, Currency.USD)

    def test_add_exchange_rate_with_different_fromCurrency_than_pivot_currency(self, bank: Bank):
        er = ExchangeRate( 1.3, Currency.USD, Currency.EUR)
        try:
            bank.addExchangeRate(er)
            assert False, "Expected ValueError to be raised"
        except ValueError as error:
            assert str(error) == "Must exchange rate from the same currency as the Bank's Pivot Currency"

    def test_convert_from_currency_to_same_currency_returns_same_money(self, bank: Bank):
        money = Money(10, Currency.EUR)
        assert bank.convert(money, Currency.EUR) == money