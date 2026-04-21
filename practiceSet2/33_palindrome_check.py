"""Question 33: Check whether a string is a palindrome."""


def is_palindrome(text: str) -> bool:
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def main() -> None:
    word = "Madam"
    print("Palindrome" if is_palindrome(word) else "Not palindrome")


if __name__ == "__main__":
    main()
