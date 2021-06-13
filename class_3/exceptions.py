class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError(f'Insufficient funds. Trying to withdraw {amount}, but balance is: {self.balance}')
        # else is optional here
        self.balance = self.balance - amount


my_bank_account = BankAccount()
print(f"My balance is: {my_bank_account.balance}")
my_bank_account.deposit(5000)
print(f"My balance is: {my_bank_account.balance}")

try:
    my_bank_account.withdraw(6000)
except ValueError:
    my_bank_account.deposit(2000)

my_bank_account.withdraw(6000)
print(my_bank_account.balance)






