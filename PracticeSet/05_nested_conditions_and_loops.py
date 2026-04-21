"""Question 5: Decision-making with nested conditions and nested loops."""  # Executes this statement.


def main() -> None:  # Defines a function.
    for row in range(1, 4):  # Starts a for loop over values.
        print(f"Row {row}:")  # Displays output to the user.
        for column in range(1, 4):  # Starts a for loop over values.
            if row % 2 == 0:  # Checks a condition.
                if column % 2 == 0:  # Checks a condition.
                    print(f"  ({row}, {column}) -> even row and even column")  # Displays output to the user.
                else:  # Runs when previous conditions are false.
                    print(f"  ({row}, {column}) -> even row and odd column")  # Displays output to the user.
            else:  # Runs when previous conditions are false.
                if column % 2 == 0:  # Checks a condition.
                    print(f"  ({row}, {column}) -> odd row and even column")  # Displays output to the user.
                else:  # Runs when previous conditions are false.
                    print(f"  ({row}, {column}) -> odd row and odd column")  # Displays output to the user.
        print()  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
