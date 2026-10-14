from collections.abc import Callable


# Create the OrderHandler type alias - accepts dictionary and returns nothing
OrderHandler = Callable[[dict], None]


# Create the OrderEvents class
# This manages subscriptions and notifications
class OrderEvents:
    def __init__(self):
        self._handlers: list[OrderHandler] = []

    # Allow handlers to subscripe
    def subscribe(self, handler: OrderHandler) -> None:
        self._handlers.append(handler)

    # Defines what happens when an event is published
    def publish(self, order: dict) -> None:
        # Loops through each registered handler and calls it
        for handler in self._handlers:
            handler(order)


# Observer functions that react to the events
def update_inventory(order: dict) -> None:
    print(f"Inventory updated for {order['id']}")

def send_confirmation(order: dict) -> None:
    print(f"Confirmation sent for {order['customer']}")


# Instantiate an empty OrderEvents object
events = OrderEvents()

# Subscript to the handlers
events.subscribe(update_inventory)
events.subscribe(send_confirmation)

# Publish a new event
events.publish({"id": 101, "customer": "Bob"})