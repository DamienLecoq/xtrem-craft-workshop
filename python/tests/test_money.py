from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.money_calculator import MoneyCalculator
from xterm_craft_workshop.money import Money

class TestMoney:
    def test_add_in_usd_returns_value(self):
        usd1 = Money(5, Currency.USD)
        usd2 = Money(10, Currency.USD)
        assert usd1.add(usd2) == Money(15, Currency.USD)

    def test_add_in_different_currency_throws_exception(self):
        usd = Money(5, Currency.USD)
        eur = Money(10, Currency.EUR)

        try:
            usd.add(eur)
            assert False, "Expected ValueError to be raised"
        except ValueError as error:
            assert str(error) == "Cannot add money with different currencies"

    def test_multiply_in_usd_returns_positive_number(self):
        usd = Money(10, Currency.USD)
        assert usd.times(2) == Money(20, Currency.USD)

    def test_divide_in_usd_returns_value(self):
        usd = Money(4002, Currency.USD)
        assert usd.divide(4) == Money(1000.5, Currency.USD)
