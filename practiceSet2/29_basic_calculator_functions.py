"""Question 29: Basic calculator operations using functions."""


def add(first: float, second: float) -> float:
    return first + second


def subtract(first: float, second: float) -> float:
    return first - second


def multiply(first: float, second: float) -> float:
    return first * second


def divide(first: float, second: float) -> float:
    return first / second


def main() -> None:
    first = 12
    second = 4
    print("Addition:", add(first, second))
    print("Subtraction:", subtract(first, second))
    print("Multiplication:", multiply(first, second))
    print("Division:", divide(first, second))


if __name__ == "__main__":
    main()
