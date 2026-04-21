"""Question 29: Basic calculator operations using functions."""  # Executes this statement.


def add(a: float, b: float) -> float:  # Defines a function.
    return a + b  # Returns a value from the function.


def subtract(a: float, b: float) -> float:  # Defines a function.
    return a - b  # Returns a value from the function.


def multiply(a: float, b: float) -> float:  # Defines a function.
    return a * b  # Returns a value from the function.


def divide(a: float, b: float) -> float:  # Defines a function.
    return a / b  # Returns a value from the function.


def main() -> None:  # Defines a function.
    first = 12  # Stores a value in variable(s).
    second = 4  # Stores a value in variable(s).
    print("Addition:", add(first, second))  # Displays output to the user.
    print("Subtraction:", subtract(first, second))  # Displays output to the user.
    print("Multiplication:", multiply(first, second))  # Displays output to the user.
    print("Division:", divide(first, second))  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
