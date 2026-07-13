class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0

    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += self.balance
    
    def get_balance(self):
        return self.balance

# TODO: Create two accounts
account_1 = BankAccount("Alice", 1000)
account_2 = BankAccount("Bob", 2000)
# TODO: Print the information using the mentioned format
print(f"Alice's balance: ${account_1.get_balance()}")
print(f"Bob's balance: ${account_2.get_balance()}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")