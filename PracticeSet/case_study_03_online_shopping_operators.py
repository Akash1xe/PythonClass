"""Case study 3: Online shopping cost, discount, and membership eligibility."""  # Executes this statement.


def main() -> None:  # Defines a function.
    quantity = 3  # Stores a value in variable(s).
    unit_price = 499.0  # Stores a value in variable(s).
    membership = True  # Stores a value in variable(s).

    subtotal = quantity * unit_price  # Stores a value in variable(s).
    discount = subtotal * 0.10 if subtotal >= 1000 else 0.0  # Stores a value in variable(s).
    if membership and subtotal >= 1500:  # Checks a condition.
        discount += subtotal * 0.05  # Executes this statement.
    total = subtotal - discount  # Stores a value in variable(s).

    print("Subtotal:", subtotal)  # Displays output to the user.
    print("Discount:", discount)  # Displays output to the user.
    print("Total payable:", total)  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
