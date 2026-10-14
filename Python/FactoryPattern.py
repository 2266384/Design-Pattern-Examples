from typing import Protocol

# Define the PaymentProvider interface - describes the expected behaviour
class PaymentProvider(Protocol):
    def charge(self, amount: float) -> str: ...

# Define the unique implementations for the interface
# These have their own implementations of 'charge' but follow the pattern
# dictated by the interface
class VisaProvider:
    def charge(self, amount: float) -> str:
        return f"Visa charged £{amount:.2f}"

class BankProvider:
    def charge(self, amount: float) -> str:
        return f"Bank transfer initiated for £{amount:.2f}"


# Create the factory class
class PaymentFactory:
    @staticmethod       # Allows create to be called on the Payment Factory without needing to instantiate it first
    def create(provider: str) -> PaymentProvider:
        providers = {
            "visa": VisaProvider,
            "bank": BankProvider,
        }
        try:
            return providers[provider.lower()]()
        except KeyError:
            raise ValueError(f"Unsupported provider: {provider}")


payment = PaymentFactory.create("visa")
print(payment.charge(49.99))

payment = PaymentFactory.create("bank")
print(payment.charge(100))