class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Balance:", self.balance)

a1 = BankAccount("Akash", 1000)

a1.deposit(500)
a1.withdraw(300)

a1.show_balance()