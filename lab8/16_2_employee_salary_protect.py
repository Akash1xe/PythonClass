class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def display(self):
        print("Salary :", self.__salary)


emp = Employee(30000)
emp.display()
