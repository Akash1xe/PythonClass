"""Question 17: Lambda functions with map() and filter()."""  # Executes this statement.


def main() -> None:  # Defines a function.
    numbers = [1, 2, 3, 4, 5, 6]  # Stores a value in variable(s).
    squares = list(map(lambda value: value * value, numbers))  # Stores a value in variable(s).
    evens = list(filter(lambda value: value % 2 == 0, numbers))  # Stores a value in variable(s).

    print("Numbers:", numbers)  # Displays output to the user.
    print("Squares using map:", squares)  # Displays output to the user.
    print("Even numbers using filter:", evens)  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
