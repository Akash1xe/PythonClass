class Area:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate(self):
        area = self.length * self.breadth
        print("Area =", area)


a = Area(6, 4)
a.calculate()
