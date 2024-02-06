class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit of {amount} successful. New balance: {self.balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal of {amount} successful. Remaining balance: {self.balance}"
        elif amount > self.balance:
            return "Insufficient funds for this withdrawal."
        else:
            return "Withdrawal amount must be positive."


account = Account("John Doe")

transactions = [
    account.deposit(100),
    account.deposit(200),
    account.withdraw(30),
    account.withdraw(300),
]

print(*transactions)
