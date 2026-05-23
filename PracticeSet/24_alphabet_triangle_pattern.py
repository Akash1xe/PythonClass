"""Question 24: Print an alphabet triangle pattern."""  # Executes this statement.


# Number of rows
n = 5

# Outer loop (rows)
for i in range(1, n + 1):
    
    # Inner loop (print alphabets)
    for j in range(i):
        print(chr(65 + j), end=" ")   # 65 = 'A'
    
    print()   # move to next line
