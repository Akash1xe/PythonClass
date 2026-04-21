"""Question 15: Dictionaries in Python and common methods."""  # Executes this statement.


def main() -> None:  # Defines a function.
    student = {"name": "Riya", "age": 19, "course": "BSc CS"}  # Stores a value in variable(s).
    print("Dictionary:", student)  # Displays output to the user.
    print("Access name:", student["name"])  # Displays output to the user.
    print("keys():", student.keys())  # Displays output to the user.
    print("values():", student.values())  # Displays output to the user.
    print("items():", student.items())  # Displays output to the user.
    student.update({"age": 20, "city": "Delhi"})  # Executes this statement.
    print("After update():", student)  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
