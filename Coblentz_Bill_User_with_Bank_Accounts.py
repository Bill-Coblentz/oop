#User with Bank Accounts - associated classes
class BankAccount:
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

class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(self.account.display_account_info())
        return self

    def transfer_money(self, receive, amount):
        self.account.withdraw(amount)
        receive.account.deposit(amount)
        print(self.account.display_account_info())
        print(receive.account.display_account_info())
        return self

bill = user("Bill Gates", "bill@msn.com")
elon = user("Elon Musk", "elon@tesla.com")
don = user("Donald Trump", "don@towers.com")

bill.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawl(100).display_user_balance()

elon.make_deposit(100).make_deposit(100).make_withdrawl(100).make_withdrawl(50).display_user_balance()

don.make_deposit(400).make_withdrawl(100).make_withdrawl(100).make_withdrawl(100).display_user_balance()

bill.transfer_money(don, 150)
