def even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"


num = int(input("Enter number: "))
print(even_odd(num))
