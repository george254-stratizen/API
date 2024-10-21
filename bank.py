import random

class User:
    def __init__(self, name):
        self.name = name
        self.user_id = random.randint(1000, 9999)
        self.accounts = []

    def create_account(self, account_type):
        new_account = Account(account_type)
        self.accounts.append(new_account)
        print(f"Account created for {self.name}: {new_account.account_number}")

    def view_accounts(self):
        print(f"Accounts for {self.name}:")
        for account in self.accounts:
            print(f" - Account Number: {account.account_number}, Type: {account.account_type}, Balance: ${account.get_balance():.2f}")

class Account:
    def __init__(self, account_type):
        self.account_number = random.randint(10000000, 99999999)
        self.balance = 0.0
        self.account_type = account_type

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f} to Account Number: {self.account_number}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from Account Number: {self.account_number}")

    def get_balance(self):
        return self.balance

class Transaction:
    def __init__(self, account, amount, transaction_type):
        self.transaction_id = random.randint(10000, 99999)
        self.amount = amount
        self.transaction_type = transaction_type
        self.account = account

    def execute(self):
        if self.transaction_type == "deposit":
            self.account.deposit(self.amount)
        elif self.transaction_type == "withdraw":
            self.account.withdraw(self.amount)
        else:
            print("Invalid transaction type.")

# Example usage
if __name__ == "__main__":
    user1 = User("Alice")
    user1.create_account("Savings")
    
    # Accessing the first account created
    account = user1.accounts[0]
    
    # Performing transactions
    transaction1 = Transaction(account, 500, "deposit")
    transaction1.execute()
    
    transaction2 = Transaction(account, 200, "withdraw")
    transaction2.execute()
    
    user1.view_accounts()