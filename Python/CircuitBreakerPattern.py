
from enum import Enum, auto


class State(Enum):
    CLOSED = auto()
    OPEN = auto()
    HALF_OPEN = auto()


class CircuitBreaker:
    def __init__(self, failure_threshold: int = 3):
        self.failure_threshold = failure_threshold
        self.failures = 0
        self.state = State.CLOSED

    def call(self, operation):
        if self.state is State.OPEN:
            raise RuntimeError("Circuit is open")

        if self.state is State.HALF_OPEN:
            raise RuntimeError("Trial call already in progress")

        try:
            result = operation()
        except Exception:
            self.failures += 1

            if self.failures >= self.failure_threshold:
                self.state = State.OPEN

            raise
        else:
            self.failures = 0
            return result

    def try_recover(self, operation):
        if self.state is not State.OPEN:
            return self.call(operation)

        self.state = State.HALF_OPEN

        try:
            result = operation()
        except Exception:
            self.state = State.OPEN
            raise
        else:
            self.failures = 0
            self.state = State.CLOSED
            return result


def unreliable_service():
    raise ConnectionError("Remote service unavailable")


breaker = CircuitBreaker(failure_threshold=3)

for attempt in range(3):
    try:
        breaker.call(unreliable_service)
    except ConnectionError:
        print(f"Failure {attempt + 1}")

print(breaker.state.name)  # OPEN

try:
    breaker.call(unreliable_service)
except RuntimeError as error:
    print(error)  # Circuit is open


def recovered_service():
    return "Service is healthy"


print(breaker.try_recover(recovered_service))
print(breaker.state.name)  # CLOSED
