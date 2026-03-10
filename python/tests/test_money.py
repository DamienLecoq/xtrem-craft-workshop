from python.src.currency import Currency
from python.src.money_calculator import MoneyCalculator

class TestMoney:
    def test_add_in_usd_returns_value(self):
        assert MoneyCalculator.add(5, Currency.USD, 10) == 15.0

    def test_multiply_in_usd_returns_positive_number(self):
        assert MoneyCalculator.times(10, Currency.USD, 2) > 0

    def test_divide_in_usd_returns_value(self):
        assert MoneyCalculator.divide(4002, Currency.USD, 4) == 1000.5
