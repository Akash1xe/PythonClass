"""Question 23: Tuple creation, indexing, slicing, and methods."""  # Executes this statement.


def main() -> None:  # Defines a function.
    values = (100, 200, 300, 400, 500)  # Stores a value in variable(s).
    print("Tuple:", values)  # Displays output to the user.
    print("Index 0:", values[0])  # Displays output to the user.
    print("Slice 1:4:", values[1:4])  # Displays output to the user.
    print("Count of 200:", values.count(200))  # Displays output to the user.
    print("Index of 300:", values.index(300))  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
