# Bank Account Simulation
# Create a BankAccount class with deposit, withdraw, and balance inquiry methods.
class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0  # starting balance is 0
    # This method adds money to the account.
    def deposit(self, amount):

        self.balance = self.balance + amount

        print("Amount deposited:", amount)
 
    def withdraw(self, amount):

        if amount <= self.balance:

            self.balance = self.balance - amount

            print("Amount withdrawn:", amount)

        else:

            print("Not enough balance to withdraw.")
 
    def check_balance(self):

        print("Current balance is:", self.balance)
 
 

my_account = BankAccount("Seema")

my_account.deposit(1000)

my_account.withdraw(500)

my_account.check_balance()
 