"""Case study 7: Ticket booking system using lists, dictionaries, operators, conditions, and functions."""  # Executes this statement.


def available_seats(seats: list[dict[str, object]]) -> list[dict[str, object]]:  # Defines a function.
    return [seat for seat in seats if seat["available"]]  # Returns a value from the function.


def calculate_fare(base_fare: float, tax_rate: float, discount_rate: float) -> float:  # Defines a function.
    taxed_amount = base_fare + (base_fare * tax_rate)  # Stores a value in variable(s).
    return taxed_amount - (taxed_amount * discount_rate)  # Returns a value from the function.


def main() -> None:  # Defines a function.
    passengers = [  # Stores a value in variable(s).
        {"name": "Asha", "seat": "A1", "available": True},  # Executes this statement.
        {"name": "Ravi", "seat": "A2", "available": False},  # Executes this statement.
        {"name": "Neha", "seat": "A3", "available": True},  # Executes this statement.
    ]  # Executes this statement.

    open_seats = available_seats(passengers)  # Stores a value in variable(s).
    fare = calculate_fare(1000.0, 0.05, 0.10)  # Stores a value in variable(s).

    print("Available seats:")  # Displays output to the user.
    for seat in open_seats:  # Starts a for loop over values.
        print(seat["seat"], seat["name"])  # Displays output to the user.

    print("Calculated fare:", fare)  # Displays output to the user.
    print("Seat booking status:", "Seats available" if open_seats else "No seats available")  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
