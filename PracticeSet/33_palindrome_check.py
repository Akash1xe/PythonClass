"""Question 33: Check whether a string is a palindrome."""  # Executes this statement.


# Taking input
s = input("Enter a string: ")

# Reverse the string
rev = s[::-1]

# Check palindrome
if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
