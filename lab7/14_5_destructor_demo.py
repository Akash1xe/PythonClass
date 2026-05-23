class Demo:
    def __init__(self):
        print("Constructor Called")

    def __del__(self):
        print("Destructor Called")


obj = Demo()
del obj
