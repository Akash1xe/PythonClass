"""Question 9: Different types of operators in Python."""  # Executes this statement.


def main() -> None:  # Defines a function.
    a = 10  # Stores a value in variable(s).
    b = 3  # Stores a value in variable(s).

    print("Arithmetic:", a + b, a - b, a * b, a / b, a // b, a % b, a ** b)  # Displays output to the user.
    print("Comparison:", a > b, a < b, a == b, a != b)  # Displays output to the user.
    print("Assignment:", end=" ")  # Displays output to the user.
    c = a  # Stores a value in variable(s).
    c += b  # Executes this statement.
    print(c)  # Displays output to the user.
    print("Logical:", a > 5 and b > 5, a > 5 or b > 5, not (a > b))  # Displays output to the user.
    print("Bitwise:", a & b, a | b, a ^ b, a << 1, a >> 1)  # Displays output to the user.
    print("Membership:", 3 in [1, 2, 3], 4 not in [1, 2, 3])  # Displays output to the user.
    print("Identity:", a is c, a is not b)  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
