class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name :", self.name)


p1 = Person("Ravi")
p2 = Person("Sita")

p1.show()
p2.show()
