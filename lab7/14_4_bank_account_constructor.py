class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn successfully")
        else:
            print("Insufficient Balance")

    def display(self):
        print("Current Balance :", self.balance)


acc = BankAccount(100)
acc.deposit(500)
acc.withdraw(300)
acc.display()
