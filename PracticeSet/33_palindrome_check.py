"""Question 33: Check whether a string is a palindrome."""  # Executes this statement.


def is_palindrome(text: str) -> bool:  # Defines a function.
    cleaned = text.replace(" ", "").lower()  # Stores a value in variable(s).
    return cleaned == cleaned[::-1]  # Returns a value from the function.


def main() -> None:  # Defines a function.
    word = "Madam"  # Stores a value in variable(s).
    print("Palindrome" if is_palindrome(word) else "Not palindrome")  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
