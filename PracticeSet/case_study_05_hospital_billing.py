"""Case study 5: Hospital billing with discount analysis."""  # Executes this statement.


def main() -> None:  # Defines a function.
    consultation = 500.0  # Stores a value in variable(s).
    medicines = 1200.0  # Stores a value in variable(s).
    room_charges = 2500.0  # Stores a value in variable(s).

    total_bill = consultation + medicines + room_charges  # Stores a value in variable(s).
    discount = total_bill * 0.08 if total_bill >= 4000 else 0.0  # Stores a value in variable(s).
    net_bill = total_bill - discount  # Stores a value in variable(s).

    print("Total bill:", total_bill)  # Displays output to the user.
    print("Discount:", discount)  # Displays output to the user.
    print("Net bill:", net_bill)  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
