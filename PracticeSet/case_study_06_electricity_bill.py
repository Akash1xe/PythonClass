"""Case study 6: Electricity bill with operator-based decision making."""  # Executes this statement.


def calculate_bill(units: int) -> float:  # Defines a function.
    if units <= 100:  # Checks a condition.
        rate = 5  # Stores a value in variable(s).
    elif units <= 200:  # Checks another condition if needed.
        rate = 7  # Stores a value in variable(s).
    else:  # Runs when previous conditions are false.
        rate = 10  # Stores a value in variable(s).
    return units * rate  # Returns a value from the function.


def main() -> None:  # Defines a function.
    units = 180  # Stores a value in variable(s).
    bill = calculate_bill(units)  # Stores a value in variable(s).
    surcharge = bill * 0.05 if units > 150 and bill > 0 else 0.0  # Stores a value in variable(s).
    total = bill + surcharge  # Stores a value in variable(s).

    print("Units consumed:", units)  # Displays output to the user.
    print("Base bill:", bill)  # Displays output to the user.
    print("Surcharge:", surcharge)  # Displays output to the user.
    print("Total bill:", total)  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
