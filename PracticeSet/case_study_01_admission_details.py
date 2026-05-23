"""Case study 1: Admission details with data types."""  # Executes this statement.


# Taking input from user

name = input("Enter student name: ")
age = int(input("Enter student age: "))
course = input("Enter course name: ")

# Displaying the details
print("\n--- Student Admission Details ---")
print("Name:", name)
print("Age:", age)
print("Course:", course)

# Displaying data types
print("\n--- Data Types of Variables ---")
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of course:", type(course))
