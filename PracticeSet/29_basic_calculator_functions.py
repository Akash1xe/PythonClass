"""Question 29: Basic calculator operations using functions."""  # Executes this statement.

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Main program
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

choice = int(input("Enter your choice: "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calling functions based on user choice
if choice == 1:
    print("Result:", add(num1, num2))

elif choice == 2:
    print("Result:", subtract(num1, num2))

elif choice == 3:
    print("Result:", multiply(num1, num2))

elif choice == 4:
    print("Result:", divide(num1, num2))

else:
    print("Invalid choice")
