# Number of students
n = int(input("Enter number of students: "))

# Outer loop (for each student)
for i in range(n):
    print("\nStudent", i + 1)

    # Input marks
    m1 = int(input("Enter marks in Subject 1: "))
    m2 = int(input("Enter marks in Subject 2: "))
    m3 = int(input("Enter marks in Subject 3: "))

    # Calculate average
    avg = (m1 + m2 + m3) / 3

    # Decision-making with nested conditions
    if m1 >= 35 and m2 >= 35 and m3 >= 35:
        if avg >= 75:
            print("Result: Distinction")
        elif avg >= 50:
            print("Result: Pass")
        else:
            print("Result: Pass (Low Marks)")
    else:
        print("Result: Fail")