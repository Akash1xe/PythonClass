"""Question 18: Functions and methods in Python."""  # Executes this statement.


def greet(name: str) -> str:  # Defines a function.
    return f"Hello, {name}!"  # Returns a value from the function.


def main() -> None:  # Defines a function.
    name = "  python  "  # Stores a value in variable(s).
    print(greet(name.strip()))  # Displays output to the user.
    print("Built-in method upper():", name.upper())  # Displays output to the user.
    print("Built-in method strip():", name.strip())  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
