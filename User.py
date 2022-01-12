#create user class
class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawl(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.account_balance)

    def transfer_money(self, receive, amount):
        self.account_balance -= amount
        receive.account_balance += amount
        print(self.account_balance)
        print(receive.account_balance)

#Create 3 instances
bill = user("Bill Gates", "bill@msn.com")
elon = user("Elon Musk", "elon@tesla.com")
don = user("Donald Trump", "don@towers.com")

bill.make_deposit(100)
bill.make_deposit(100)
bill.make_deposit(100)
bill.make_withdrawl(100)
bill.display_user_balance()

elon.make_deposit(100)
elon.make_deposit(100)
elon.make_withdrawl(100)
elon.make_withdrawl(50)
elon.display_user_balance()

don.make_deposit(400)
don.make_withdrawl(100)
don.make_withdrawl(100)
don.make_withdrawl(100)
don.display_user_balance()

bill.transfer_money(don, 150)