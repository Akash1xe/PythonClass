"""Question 25: Print a pyramid pattern using numbers."""


def main() -> None:
    rows = 5
    for row in range(1, rows + 1):
        print(" " * (rows - row), end="")
        for column in range(1, row + 1):
            print(column, end=" ")
        print()


if __name__ == "__main__":
    main()
