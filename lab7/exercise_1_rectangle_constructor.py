class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def display(self):
        print("Length :", self.length)
        print("Breadth :", self.breadth)


r = Rectangle(10, 5)
r.display()
