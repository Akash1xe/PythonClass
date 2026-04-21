def sum_digits(n):
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    return s


num = int(input("Enter number: "))
print("Sum of digits:", sum_digits(num))
