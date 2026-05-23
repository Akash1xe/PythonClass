# Taking input
m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))

# Calculating total and average
total = m1 + m2 + m3
average = total / 3

# Display total and average
print("\nTotal Marks:", total)
print("Average Marks:", average)

# Determining grade
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"

# Pass/Fail condition
if m1 < 35 or m2 < 35 or m3 < 35:
    status = "Fail"
else:
    status = "Pass"

# Final Output
print("\nGrade:", grade)
print("Result Status:", status)