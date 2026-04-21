"""Question 30: Check whether a number is even or odd using functions."""  # Executes this statement.


def is_even(number: int) -> bool:  # Defines a function.
    return number % 2 == 0  # Returns a value from the function.


def main() -> None:  # Defines a function.
    number = 11  # Stores a value in variable(s).
    if is_even(number):  # Checks a condition.
        print("Even")  # Displays output to the user.
    else:  # Runs when previous conditions are false.
        print("Odd")  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
