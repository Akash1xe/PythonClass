"""Question 25: Print a pyramid pattern using numbers or symbols."""  # Executes this statement.


def main() -> None:  # Defines a function.
    rows = 5  # Stores a value in variable(s).
    for row in range(1, rows + 1):  # Starts a for loop over values.
        print(" " * (rows - row), end="")  # Displays output to the user.
        for column in range(1, row + 1):  # Starts a for loop over values.
            print(column, end=" ")  # Displays output to the user.
        print()  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
