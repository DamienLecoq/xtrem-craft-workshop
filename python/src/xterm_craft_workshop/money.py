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
        if value < 0:
            raise ValueError("Multiplication by a negative value is not possible")
        return Money(self.amount * value, self.currency)
    
    def divide(self, value: int) -> "Money":
        if value == 0:
            raise ValueError("Division by zero is not possible")
        return Money(self.amount / value, self.currency)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency

    def getMoney(self) -> float:
        return self.amount
    
    def getCurrency(self) -> Currency:
        return self.currency
    
    def __add__(self, other: "Money") -> "Money":
        return self.add(other)
        
    

# doit etre immutable, on init qu'une fois
# mettre des guards , pas monaie negative, pas de division par 0, pas de multiplication par negative, pas ajouter monnaies dans des monnaies differentes, pas pvr créer un billet de 30
# faire refacto dans le code, on enleve "montant" on mets juste money
# refacto les tests, on utilise Money 
