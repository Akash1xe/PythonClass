"""Question 4: Valid and invalid identifiers, keywords, and indentation."""  # Executes this statement.


def main() -> None:  # Defines a function.
    valid_identifiers = ["name", "student1", "total_marks", "_value"]  # Stores a value in variable(s).
    invalid_identifiers = ["1name", "total-marks", "class", "my name"]  # Stores a value in variable(s).

    print("Valid identifiers:")  # Displays output to the user.
    for identifier in valid_identifiers:  # Starts a for loop over values.
        print("-", identifier)  # Displays output to the user.

    print()  # Displays output to the user.
    print("Invalid identifiers:")  # Displays output to the user.
    for identifier in invalid_identifiers:  # Starts a for loop over values.
        print("-", identifier)  # Displays output to the user.

    print()  # Displays output to the user.
    score = 85  # Stores a value in variable(s).
    if score >= 50:  # Checks a condition.
        print("if keyword example: Pass")  # Displays output to the user.
    else:  # Runs when previous conditions are false.
        print("if keyword example: Fail")  # Displays output to the user.

    print("else keyword also shown above with proper indentation.")  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
