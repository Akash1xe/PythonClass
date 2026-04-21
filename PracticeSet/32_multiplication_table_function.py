"""Question 32: Generate multiplication table using a function."""  # Executes this statement.


def multiplication_table(number: int) -> None:  # Defines a function.
    for multiplier in range(1, 11):  # Starts a for loop over values.
        print(f"{number} x {multiplier} = {number * multiplier}")  # Displays output to the user.


def main() -> None:  # Defines a function.
    multiplication_table(7)  # Executes this statement.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
