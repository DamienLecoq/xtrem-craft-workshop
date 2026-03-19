from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.money import Money  
from typing import Dict

class CreateBankBuilder:
    _exchange_rate: Dict[str, float] = {}
    def __init__(self, exchange_rate = {}):
        self._exchange_rate = exchange_rate

    def ABank(self):
        return CreateBankBuilder()
    
    def WithExchangeRate(self, fromCurrency: Currency, toCurrency: Currency, rate: float) -> "CreateBankBuilder":
        self._exchange_rate[f'{fromCurrency.value}->{toCurrency.value}'] = rate
        return self
    
    def build(self) -> "CreateBankBuilder":
        return Bank(exchange_rate=self._exchange_rate)

 

    


