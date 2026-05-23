# Taking input from user and converting it into float (decimal number)
units = float(input("Enter units consumed: "))

# Initializing bill variable with 0 (starting value)
bill = 0

# Checking if units are less than or equal to 100 (first slab)
if units <= 100:
    # Multiply total units with rate ₹1.5 per unit
    bill = units * 1.5

# Checking if units are between 101 and 200 (second slab)
elif units <= 200:
    # First 100 units at ₹1.5 + remaining units at ₹2.5
    bill = (100 * 1.5) + (units - 100) * 2.5

# Checking if units are between 201 and 300 (third slab)
elif units <= 300:
    # First 100 units at ₹1.5 + next 100 at ₹2.5 + remaining at ₹4.0
    bill = (100 * 1.5) + (100 * 2.5) + (units - 200) * 4.0

# If units are more than 300 (fourth slab)
else:
    # First 100 at ₹1.5 + next 100 at ₹2.5 + next 100 at ₹4.0 + remaining at ₹6.0
    bill = (100 * 1.5) + (100 * 2.5) + (100 * 4.0) + (units - 300) * 6.0

# Checking if bill is greater than 1000 for surcharge
if bill > 1000:
    # Adding 10% surcharge to bill using assignment operator (+=)
    bill += bill * 0.10

# Printing final bill with a new line before output
print("\nTotal Electricity Bill:", bill)