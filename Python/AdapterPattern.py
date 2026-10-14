from typing import Protocol

# Define the PriceProvider interface - describes the expected behaviour
class PriceProvider(Protocol):
    def get_price(self, product_id: str) -> float: ...


# Class the simulates and external supplier API
class SupplierAPI:
    def fetch_product(self, sku: str) -> dict:
        return {"sku": sku, "price_pence": 1299}


# Adapter to handle the Supplier API - converts price to the expected format
# If the supplier changes the price format the SupplierPriceAdapter will need to be
# modified to ensure the output is in the correct format
# This removes the need to update the rest of the code by normalising the data
class SupplierPriceAdapter:
    def __init__(self, supplier: SupplierAPI):
        self.supplier = supplier

    def get_price(self, product_id: str) -> float:
        product = self.supplier.fetch_product(product_id)
        return product["price_pence"] / 100


def display_price(provider: PriceProvider, product_id: str) -> None:
    print(f"Price: £{provider.get_price(product_id):.2f}")


supplier = SupplierAPI()
adapter = SupplierPriceAdapter(supplier)

display_price(adapter, "SKU-123")