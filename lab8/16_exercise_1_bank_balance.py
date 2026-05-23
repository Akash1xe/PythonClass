class Bank:
    def __init__(self):
        self.__balance = 0

    def set_balance(self, amount):
        self.__balance = amount

    def get_balance(self):
        return self.__balance


b = Bank()
b.set_balance(5000)
print("Balance :", b.get_balance())
