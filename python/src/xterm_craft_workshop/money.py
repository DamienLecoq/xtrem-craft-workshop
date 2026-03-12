from xterm_craft_workshop.currency import Currency

class Money:
    def __init__(self, amount: float, currency: Currency):
        self.amount = amount
        self.currency = currency
        
    def add(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise ValueError("Cannot add money with different currencies")
        return Money(self.amount + other.amount, self.currency)
    
    def times(self, value: int) -> "Money":
        return Money(self.amount * value, self.currency)
    
    def divide(self, value: int) -> "Money":
        return Money(self.amount / value, self.currency)
    
