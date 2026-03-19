from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.portfolio import Portfolio
from xterm_craft_workshop.money import Money


class CreatePortfolioBuilder:
    _moneyList: list = []

    def init(self, moneyList=[]):
        self._moneyList = list(moneyList)

    def APortfolio(self):
        return CreatePortfolioBuilder()

    def WithMoney(self, amount: float, currency: Currency) -> "CreatePortfolioBuilder":
        new_list = list(self._moneyList)
        new_list.append(Money(amount, currency))
        return CreatePortfolioBuilder(new_list)

    def build(self) -> Portfolio:
        portfolio = Portfolio()
        for money in self._moneyList:
            portfolio.addMoney(money)
        return portfolio