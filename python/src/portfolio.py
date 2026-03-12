from typing import Dict
from .currency import Currency
from .bank import Bank

class Portfolio:

    def __init__(self, currency : Currency):
        self.currency = currency
        self.totalMoney = 0

    def __init__(self, currency : Currency, initMoney : int):
        self.currency = currency
        self.totalMoney = initMoney

    def addMoney(self, money : int) : 
        self.totalMoney += money

    def getMoney(self):
        return self.totalMoney
    
    def evaluateCurrency(self, bank : Bank, destCurrency : Currency):
        return bank.convert(self.totalMoney, self.currency, destCurrency)