from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.portfolio import Portfolio
from xterm_craft_workshop.money import Money


class CreatePortfolioBuilder:
    _moneyList: list = []

    def __init__(self, moneyList=[]):
        self._moneyList = list(moneyList)

    def APortfolio(self):
        return CreatePortfolioBuilder()

    def WithMoney(self, amount: float, currency: Currency) -> "CreatePortfolioBuilder":
        self._moneyList.append(Money(amount, currency))
        return self

    def build(self) -> Portfolio:
        portfolio = Portfolio()
        for money in self._moneyList:
            portfolio.addMoney(money)
        return portfolio