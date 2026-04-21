"""Case study 1: Admission details with data types."""  # Executes this statement.


def main() -> None:  # Defines a function.
    name = input("Enter student name: ")  # Reads input from the user.
    age = int(input("Enter age: "))  # Stores a value in variable(s).
    course = input("Enter course: ")  # Reads input from the user.

    print("Student details:")  # Displays output to the user.
    print("Name:", name, type(name))  # Displays output to the user.
    print("Age:", age, type(age))  # Displays output to the user.
    print("Course:", course, type(course))  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
