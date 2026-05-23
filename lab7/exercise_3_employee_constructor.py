class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name :", self.name)
        print("Salary :", self.salary)

name = input("Enter employee name : ")
salary = int(input("Enter salary : "))

e1 = Employee(name, salary)
e1.display()
