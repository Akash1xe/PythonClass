class Student:
    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks


s = Student(85)
print("Marks :", s.get_marks())
