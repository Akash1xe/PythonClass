"""Case study 4: Student record management with total, average, grade, and pass/fail."""  # Executes this statement.


def grade_from_average(average: float) -> str:  # Defines a function.
    if average >= 90:  # Checks a condition.
        return "A"  # Returns a value from the function.
    if average >= 75:  # Checks a condition.
        return "B"  # Returns a value from the function.
    if average >= 60:  # Checks a condition.
        return "C"  # Returns a value from the function.
    if average >= 40:  # Checks a condition.
        return "D"  # Returns a value from the function.
    return "F"  # Returns a value from the function.


def main() -> None:  # Defines a function.
    marks = [78, 84, 91]  # Stores a value in variable(s).
    total = sum(marks)  # Stores a value in variable(s).
    average = total / len(marks)  # Stores a value in variable(s).
    grade = grade_from_average(average)  # Stores a value in variable(s).
    passed = all(mark >= 40 for mark in marks)  # Stores a value in variable(s).

    print("Marks:", marks)  # Displays output to the user.
    print("Total:", total)  # Displays output to the user.
    print("Average:", average)  # Displays output to the user.
    print("Grade:", grade)  # Displays output to the user.
    print("Result:", "Pass" if passed else "Fail")  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
