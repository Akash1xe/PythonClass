"""Question 25: Print a pyramid pattern using numbers or symbols."""  # Executes this statement.


n = 5

for i in range(1, n + 1):
    
    # spaces
    for j in range(n - i):
        print(" ", end="")
    
    # numbers
    for k in range(1, i + 1):
        print(k, end=" ")
    
    print()
