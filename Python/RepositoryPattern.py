from dataclasses import dataclass


# Create a Customer data class
@dataclass
class Customer:
    id: int
    name: str

# In-memory Customer Repository
class CustomerRepository:
    def __init__(self):
        self._customers = {
            1: Customer(1, "Fred"),
            2: Customer(2, "Bob")
        }

    # Get the customer by their id
    def get_by_id(self, customer_id: int) -> Customer | None:
        return self._customers.get(customer_id)

    # Create a new customer record
    def add(self, customer: Customer) -> None:
        self._customers[customer.id] = customer


# Create a Customer Service Class
class CustomerService:
    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def get_customer_name(self, customer_id: int) -> str:
        customer = self.repository.get_by_id(customer_id)
        if customer is None:
            raise ValueError("Customer not found")
        return customer.name


# Instantiate the repository
repo = CustomerRepository()

# Instantiate the service using the repository
service = CustomerService(repo)


# Example code
print(service.get_customer_name(1))
repo.add(Customer(3, "Alice"))
print(service.get_customer_name(3))