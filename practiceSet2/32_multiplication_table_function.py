"""Question 32: Generate multiplication table using a function."""


def multiplication_table(number: int) -> None:
    for multiplier in range(1, 11):
        print(f"{number} x {multiplier} = {number * multiplier}")


def main() -> None:
    multiplication_table(7)


if __name__ == "__main__":
    main()
