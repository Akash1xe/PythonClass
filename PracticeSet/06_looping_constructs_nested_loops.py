"""Question 6: Looping constructs using for and while with nested loops."""  # Executes this statement.


def for_loop_pattern() -> None:  # Defines a function.
    for outer in range(1, 4):  # Starts a for loop over values.
        for inner in range(1, outer + 1):  # Starts a for loop over values.
            print(inner, end=" ")  # Displays output to the user.
        print()  # Displays output to the user.


def while_loop_pattern() -> None:  # Defines a function.
    outer = 1  # Stores a value in variable(s).
    while outer <= 3:  # Starts a while loop.
        inner = 1  # Stores a value in variable(s).
        while inner <= outer:  # Starts a while loop.
            print("*", end=" ")  # Displays output to the user.
            inner += 1  # Executes this statement.
        print()  # Displays output to the user.
        outer += 1  # Executes this statement.


def main() -> None:  # Defines a function.
    print("For-loop nested output:")  # Displays output to the user.
    for_loop_pattern()  # Executes this statement.
    print()  # Displays output to the user.
    print("While-loop nested output:")  # Displays output to the user.
    while_loop_pattern()  # Executes this statement.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
