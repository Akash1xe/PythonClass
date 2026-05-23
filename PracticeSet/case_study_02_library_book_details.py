"""Case study 2: Library book details with data types."""  # Executes this statement.


# Taking input from user

title = input("Enter book title: ")
author = input("Enter author name: ")
price = float(input("Enter book price: "))

# Displaying book details
print("\n--- Book Details ---")
print("Title:", title)
print("Author:", author)
print("Price:", price)

# Displaying data types
print("\n--- Data Types of Variables ---")
print("Type of title:", type(title))
print("Type of author:", type(author))
print("Type of price:", type(price))
