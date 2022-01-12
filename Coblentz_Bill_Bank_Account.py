#from _typeshed import Self


class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = 1.05
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        elif self.balance < amount:
            self.balance = self.balance - 5
            print("Insufficient funds: Chargint a $5 fee")
        return self
    
    def display_account_info(self):
        print("Balance: $" + str(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= self.int_rate
            return self

account_1 = BankAccount(1.05, 100)
account_2 = BankAccount(1.05, 500)

account_1.deposit(100).deposit(100).deposit(100).withdraw(450).yield_interest().display_account_info()
account_2.deposit(200).deposit(200).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()