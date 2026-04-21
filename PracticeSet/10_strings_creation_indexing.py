"""Question 10: Strings, creation, and indexing."""  # Executes this statement.


def main() -> None:  # Defines a function.
    text1 = "Python"  # Stores a value in variable(s).
    text2 = 'Programming'  # Stores a value in variable(s).
    text3 = """Strings can also be written using triple quotes."""  # Stores a value in variable(s).

    print(text1)  # Displays output to the user.
    print(text2)  # Displays output to the user.
    print(text3)  # Displays output to the user.
    print("First character:", text1[0])  # Displays output to the user.
    print("Last character:", text2[-1])  # Displays output to the user.
    print("Slice:", text1[1:4])  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
