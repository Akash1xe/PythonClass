class Employee:
    def __init__(self, name, basic):
        self.name = name
        self.basic = basic

    def calculate_salary(self):
        hra = 0.2 * self.basic
        da = 0.1 * self.basic
        total = self.basic + hra + da
        return total


e1 = Employee("Arun", 20000)
print("Total Salary :", e1.calculate_salary())
