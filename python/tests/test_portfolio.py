import pytest

from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError
from xterm_craft_workshop.portfolio import Portfolio
from xterm_craft_workshop.money import Money


@pytest.fixture
def bank() -> Bank:
    return Bank.create(Currency.EUR, Currency.USD, 1.2)


@pytest.fixture
def eur_portfolio() -> Portfolio:
    return Portfolio()


class TestPortfolio:
    def test_get_money_returns_initial_amount(self):
        portfolio = Portfolio(Currency.EUR, 100)
        money = Money(100, Currency.EUR)
        assert portfolio.getMoney() == [money]

    def test_get_money_returns_zero_when_init_with_zero(self, eur_portfolio: Portfolio):
        assert eur_portfolio.getMoney() == []

    def test_add_money_increase_total(self, eur_portfolio: Portfolio):
        eur_portfolio.addMoney(Money(50, Currency.EUR))
        assert eur_portfolio.getMoney() == [Money(50, Currency.EUR)]

    def test_add_money_multiple_times(self, eur_portfolio: Portfolio):
        eur_portfolio.addMoney(Money(30, Currency.EUR))
        eur_portfolio.addMoney(Money(20, Currency.EUR))
        assert eur_portfolio.getMoney() == [Money(30, Currency.EUR), Money(20, Currency.EUR)]

    def test_evaluate_currency_same_currency_return_same_amount(self, bank: Bank):
        portfolio = Portfolio(Currency.EUR, 100)
        assert portfolio.evaluateCurrency(bank, Currency.EUR) == [Money(100, Currency.EUR)]

    def test_evaluate_currency_convert_dest_currency(self, bank: Bank):
        portfolio = Portfolio(Currency.EUR, 10)
        assert portfolio.evaluateCurrency(bank, Currency.USD) == [Money(12, Currency.USD)]

    def test_evaluate_currency_after_add(self, bank: Bank):
        portfolio = Portfolio(Currency.EUR, 10)
        portfolio.addMoney(Money(10, Currency.EUR))
        assert portfolio.evaluateCurrency(bank, Currency.USD) == [Money(12, Currency.USD), Money(12, Currency.USD)]

    def test_evaluate_currency_missing_rate_raises_exception(self, bank: Bank):
        portfolio = Portfolio(Currency.EUR, 10)
        with pytest.raises(MissingExchangeRateError) as error:
            portfolio.evaluateCurrency(bank, Currency.KRW)
        assert str(error.value) == "There is an exchange error from EUR to KRW"
