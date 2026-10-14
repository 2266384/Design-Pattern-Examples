# Command Query Responsibility Segregation

from dataclasses import dataclass

# Create and Account class
@dataclass(frozen=True)
class Account:
    id: int
    balance: float


# In memory database containing sample accounts
class AccountStore:
    def __init__(self):
        self._accounts = {
            1: Account(id=1, balance=100)
        }

    # Command: changes state
    def deposit(self, account_id: int, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive")

        account = self._accounts[account_id]
        self._accounts[account_id] = Account(
            id = account.id,
            balance = account.balance + amount
        )

    #Query: return information without changing state
    def get_balance(self, account_id: int) -> float:
        return self._accounts[account_id].balance

class DepositHandler:
    def __init__(self, store: AccountStore):
        self.store = store

    def execute(self, account_id: int, amount: float) -> None:
        self.store.deposit(account_id, amount)


class BalanceQuery:
    def __init__(self, store: AccountStore):
        self.store = store

    def execute(self, account_id: int) -> float:
        return self.store.get_balance(account_id)


store = AccountStore()
deposit = DepositHandler(store)
balance = BalanceQuery(store)


print(f"Balance of account 1: £{balance.execute(1):.2f}")
print("Depositing £50.00")
deposit.execute(1, 50)
print(f"Balance of account 1: £{balance.execute(1):.2f}")