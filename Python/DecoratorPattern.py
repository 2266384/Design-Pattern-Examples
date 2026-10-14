from typing import Protocol

# Define the PriceCalculator interface - describes the expected behaviour
class PriceCalculator(Protocol):
    def calculate(self) -> float: ...


class ProductPrice:
    def __init__(self, price: float):
        self.price = price

    def calculate(self) -> float:
        return self.price


class PriceDecorator:
    def __init__(self, price_calculator: PriceCalculator):
        self.price_calculator = price_calculator

    def calculate(self) -> float:
        return self.price_calculator.calculate()


class DiscountDecorator(PriceDecorator):
    def __init__(self, price_calculator: PriceCalculator, discount_percent: float):
        super().__init__(price_calculator)
        self.discount_percent = discount_percent

    def calculate(self) -> float:
        price = super().calculate()
        return price * (1 - self.discount_percent / 100)


class DeliveryDecorator(PriceDecorator):
    def __init__(self, price_calculator: PriceCalculator, delivery_cost: float):
        super().__init__(price_calculator)
        self.delivery_cost = delivery_cost

    def calculate(self) -> float:
        return super().calculate() + self.delivery_cost


class VatDecorator(PriceDecorator):
    def __init__(self, price_calculator: PriceCalculator, vat_percent: float):
        super().__init__(price_calculator)
        self.vat_percent = vat_percent

    def calculate(self) -> float:
        price = super().calculate()
        return price * (1+ self.vat_percent / 100)


# Create an instance of Product with a price of £100
product = ProductPrice(100)
discounted = DiscountDecorator(product, 10)         # Discounted by 10%
with_delivery = DeliveryDecorator(discounted, 5)    # With £5 delivery charge
final_price = VatDecorator(with_delivery, 20)       # Apply 20% vat

print(f"Product price: £{product.calculate():.2f}")
print(f"Discounted price: £{discounted.calculate():.2f}")
print(f"With delivery: £{with_delivery.calculate():.2f}")
print(f"Final price (inc VAT): £{final_price.calculate():.2f}")


# Same as above but nested
final_price = VatDecorator(
    DeliveryDecorator(
        DiscountDecorator(
            ProductPrice(100),
            discount_percent=10,
        ),
        delivery_cost=5,
    ),
    vat_percent=20,
)

print(f"Final price (inc VAT): £{final_price.calculate():.2f}")


# Same as the original implementation but we update the price variable each time
price = ProductPrice(100)

price = DiscountDecorator(price, 10)
price = DeliveryDecorator(price, 5)
price = VatDecorator(price, 20)

print(f"Final price (inc VAT): £{price.calculate():.2f}")