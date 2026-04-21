"""Question 12: Built-in string methods."""  # Executes this statement.


def main() -> None:  # Defines a function.
    text = "  Python Programming  "  # Stores a value in variable(s).
    print("Original:", repr(text))  # Displays output to the user.
    print("strip():", text.strip())  # Displays output to the user.
    print("lower():", text.lower())  # Displays output to the user.
    print("upper():", text.upper())  # Displays output to the user.
    print("title():", text.title())  # Displays output to the user.
    print("replace():", text.replace("Programming", "Language"))  # Displays output to the user.
    print("split():", text.split())  # Displays output to the user.
    print("find():", text.find("thon"))  # Displays output to the user.
    print("count():", text.count("o"))  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
