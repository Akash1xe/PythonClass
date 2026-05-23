# Using FOR loop with nested loop
print("Using for loop:")

for i in range(1, 6):        # outer loop
    for j in range(1, i+1):  # inner loop
        print(j, end=" ")
    print()   # new line


# Using WHILE loop with nested loop
print("\nUsing while loop:")

i = 1
while i <= 5:                # outer loop
    j = 1
    while j <= i:            # inner loop
        print(j, end=" ")
        j += 1               # increment inner loop
    print()                  # new line
    i += 1                   # increment outer loop