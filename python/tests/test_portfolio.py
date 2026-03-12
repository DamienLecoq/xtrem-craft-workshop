import pytest

from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError
from xterm_craft_workshop.portfolio import Portfolio


@pytest.fixture
def bank() -> Bank:
    return Bank.create(Currency.EUR, Currency.USD, 1.2)


@pytest.fixture
def eur_portfolio() -> Portfolio:
    return Portfolio(Currency.EUR, 0)


class TestPortfolio:
    def test_get_money_returns_initial_amount(self):
        portfolio = Portfolio(Currency.EUR, 100)
        assert portfolio.getMoney() == 100

    def test_get_money_returns_zero_when_init_with_zero(self, eur_portfolio: Portfolio):
        assert eur_portfolio.getMoney() == 0

    def test_add_money_increase_total(self, eur_portfolio: Portfolio):
        eur_portfolio.addMoney(50)
        assert eur_portfolio.getMoney() == 50

    def test_add_money_multiple_times(self, eur_portfolio: Portfolio):
        eur_portfolio.addMoney(30)
        eur_portfolio.addMoney(20)
        assert eur_portfolio.getMoney() == 50

    def test_evaluate_currency_same_currency_return_same_amount(self, bank: Bank):
        portfolio = Portfolio(Currency.EUR, 100)
        assert portfolio.evaluateCurrency(bank, Currency.EUR) == 100

    def test_evaluate_currency_convert_dest_currency(self, bank: Bank):
        portfolio = Portfolio(Currency.EUR, 10)
        assert portfolio.evaluateCurrency(bank, Currency.USD) == 12

    def test_evaluate_currency_after_add(self, bank: Bank):
        portfolio = Portfolio(Currency.EUR, 10)
        portfolio.addMoney(10)
        assert portfolio.evaluateCurrency(bank, Currency.USD) == 24

    def test_evaluate_currency_missing_rate_raises_exception(self, bank: Bank):
        portfolio = Portfolio(Currency.EUR, 10)
        with pytest.raises(MissingExchangeRateError) as error:
            portfolio.evaluateCurrency(bank, Currency.KRW)
        assert str(error.value) == "There is an exchange error from EUR to KRW"
