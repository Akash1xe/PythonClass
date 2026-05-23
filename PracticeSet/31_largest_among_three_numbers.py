"""Question 31: Largest among three numbers."""  # Executes this statement.


# Taking input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Checking largest using if-elif-else
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

# Output
print("Largest number is:", largest)
