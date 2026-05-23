class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print("Book Title :", self.title)
        print("Author :", self.author)


b1 = Book("Python Basics", "R.K. Sharma")
b1.display()
