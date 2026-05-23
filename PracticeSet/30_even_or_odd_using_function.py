"""Question 30: Check whether a number is even or odd using functions."""  # Executes this statement.


# Function to check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Main program
n = int(input("Enter a number: "))

# Function call
result = check_even_odd(n)

# Output
print("The number is:", result)
