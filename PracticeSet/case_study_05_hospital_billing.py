# Taking input
consultation = float(input("Enter consultation fee: "))
medicines = float(input("Enter medicine charges: "))
room = float(input("Enter room charges: "))
patient_type = input("Enter patient type (normal/senior): ")

# Calculating total bill
total = consultation + medicines + room
print("\nTotal Bill before discount:", total)

# Applying discount
discount = 0

# Condition 1: High bill discount
if total > 5000:
    discount += total * 0.10   # 10%

# Condition 2: Senior citizen discount
if patient_type.lower() == "senior":
    discount += total * 0.05   # 5%

# Final bill
final_bill = total - discount

# Output
print("Total Discount:", discount)
print("Final Bill Amount:", final_bill)