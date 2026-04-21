"""Question 16: Access, add, and modify elements in a dictionary."""  # Executes this statement.


def main() -> None:  # Defines a function.
    record = {"name": "Amit", "age": 21}  # Stores a value in variable(s).
    print("Original:", record)  # Displays output to the user.
    print("Access name:", record["name"])  # Displays output to the user.
    record["course"] = "BCA"  # Executes this statement.
    record["age"] = 22  # Executes this statement.
    print("After add/modify:", record)  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
