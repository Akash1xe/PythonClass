"""Question 32: Generate multiplication table using a function."""  # Executes this statement.


# Function to generate table
def multiplication_table(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

# Main program
n = int(input("Enter a number: "))

# Function call
multiplication_table(n)
