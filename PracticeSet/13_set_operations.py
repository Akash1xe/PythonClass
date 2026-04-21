"""Question 13: Set operations with examples."""  # Executes this statement.


def main() -> None:  # Defines a function.
    a = {1, 2, 3, 4}  # Stores a value in variable(s).
    b = {3, 4, 5, 6}  # Stores a value in variable(s).

    print("Union:", a | b)  # Displays output to the user.
    print("Intersection:", a & b)  # Displays output to the user.
    print("Difference:", a - b)  # Displays output to the user.
    print("Symmetric difference:", a ^ b)  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
