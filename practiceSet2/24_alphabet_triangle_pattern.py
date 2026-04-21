"""Question 24: Print an alphabet triangle pattern."""


def main() -> None:
    rows = 5
    for row in range(1, rows + 1):
        for column in range(row):
            print(chr(65 + column), end=" ")
        print()


if __name__ == "__main__":
    main()
