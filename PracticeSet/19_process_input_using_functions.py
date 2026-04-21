"""Question 19: Process input data using functions and display the result."""  # Executes this statement.


def calculate_total_and_average(marks: list[float]) -> tuple[float, float]:  # Defines a function.
    total = sum(marks)  # Stores a value in variable(s).
    average = total / len(marks)  # Stores a value in variable(s).
    return total, average  # Returns a value from the function.


def main() -> None:  # Defines a function.
    values = [78, 85, 90]  # Stores a value in variable(s).
    total, average = calculate_total_and_average(values)  # Stores a value in variable(s).
    print("Marks:", values)  # Displays output to the user.
    print("Total:", total)  # Displays output to the user.
    print("Average:", average)  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
