"""Case study 3: Online shopping cost, discount, and membership eligibility."""  # Executes this statement.


# Taking inputs
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
member = input("Are you a member? (yes/no): ")

# Calculating total cost
total = price * quantity
print("\nTotal cost before discount:", total)

# Applying discount
discount = 0

# Condition 1: total amount discount
if total > 1000:
    discount += total * 0.10   # 10% discount

# Condition 2: membership discount
if member.lower() == "yes":
    discount += total * 0.05   # extra 5% discount

# Final amount
final_amount = total - discount

# Output
print("Total discount:", discount)
print("Final amount to pay:", final_amount)