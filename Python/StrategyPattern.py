from typing import Protocol

# Define the DiscountStrategy interface - describes the expected behaviour
class DiscountStrategy(Protocol):
    def calculate(self, amount: float) -> float: ...

class NoDiscount:
    def calculate(self, amount: float) -> float:
        return amount * 1.00

class StandardDiscount:
    def calculate(self, amount: float) -> float:
        return amount * 0.90

class LoyaltyDiscount:
    def calculate(self, amount: float) -> float:
        return amount * 0.80


# Create the service class
class CheckoutService:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def checkout(self, amount: float) -> float:
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        return self.strategy.calculate(amount)


# Call the checkout service with the different strategies
print(CheckoutService(NoDiscount()).checkout(100))
print(CheckoutService(StandardDiscount()).checkout(100))
print(CheckoutService(LoyaltyDiscount()).checkout(100))