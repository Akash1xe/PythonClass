"""Question 30: Check whether a number is even or odd using a function."""


def is_even(number: int) -> bool:
    return number % 2 == 0


def main() -> None:
    number = 11
    print("Even" if is_even(number) else "Odd")


if __name__ == "__main__":
    main()
