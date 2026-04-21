"""Question 24: Print an alphabet triangle pattern."""  # Executes this statement.


def main() -> None:  # Defines a function.
    rows = 5  # Stores a value in variable(s).
    for row in range(1, rows + 1):  # Starts a for loop over values.
        for column in range(row):  # Starts a for loop over values.
            print(chr(65 + column), end=" ")  # Displays output to the user.
        print()  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
