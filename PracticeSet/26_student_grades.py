"""Question 26: Display student grades based on marks."""  # Executes this statement.


def grade_from_marks(marks: int) -> str:  # Defines a function.
    if marks >= 90:  # Checks a condition.
        return "A"  # Returns a value from the function.
    if marks >= 75:  # Checks a condition.
        return "B"  # Returns a value from the function.
    if marks >= 60:  # Checks a condition.
        return "C"  # Returns a value from the function.
    if marks >= 40:  # Checks a condition.
        return "D"  # Returns a value from the function.
    return "F"  # Returns a value from the function.


def main() -> None:  # Defines a function.
    marks = 82  # Stores a value in variable(s).
    print("Marks:", marks)  # Displays output to the user.
    print("Grade:", grade_from_marks(marks))  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
