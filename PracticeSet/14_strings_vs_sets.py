"""Question 14: Differences between strings and sets."""  # Executes this statement.


def main() -> None:  # Defines a function.
    text = "banana"  # Stores a value in variable(s).
    fruits = {"banana", "apple", "orange"}  # Stores a value in variable(s).

    print("String:", text)  # Displays output to the user.
    print("String supports indexing:", text[0])  # Displays output to the user.
    print("String keeps order and duplicates:", list(text))  # Displays output to the user.
    print()  # Displays output to the user.
    print("Set:", fruits)  # Displays output to the user.
    print("Set is unordered and stores unique items only")  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
