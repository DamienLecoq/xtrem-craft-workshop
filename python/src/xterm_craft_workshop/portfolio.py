from typing import Dict
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.money import Money    

class Portfolio:

    def __init__(self, currency : Currency = None, initMoney : int = None):
        self.moneyList = []
        if currency is not None and initMoney is not None:
            self.moneyList.append(Money(initMoney, currency))

    def addMoney(self, money : Money): 
        self.moneyList.append(money)

    def getMoney(self):
        return self.moneyList

    def evaluateCurrency(self, bank : Bank, destCurrency : Currency):
        return [bank.convert(money = m, toCurrency = destCurrency) for m in self.moneyList]