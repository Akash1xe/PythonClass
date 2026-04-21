"""Question 22: List creation, indexing, slicing, and methods."""  # Executes this statement.


def main() -> None:  # Defines a function.
    items = [10, 20, 30, 40, 50]  # Stores a value in variable(s).
    print("List:", items)  # Displays output to the user.
    print("Index 0:", items[0])  # Displays output to the user.
    print("Slice 1:4:", items[1:4])  # Displays output to the user.
    items.append(60)  # Executes this statement.
    items.insert(1, 15)  # Executes this statement.
    items.remove(30)  # Executes this statement.
    last_item = items.pop()  # Stores a value in variable(s).
    print("After methods:", items)  # Displays output to the user.
    print("Popped item:", last_item)  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
