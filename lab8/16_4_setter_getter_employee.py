class Employee:
    def __init__(self):
        self.__salary = 0

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary


emp = Employee()
emp.set_salary(40000)
print("Salary :", emp.get_salary())
