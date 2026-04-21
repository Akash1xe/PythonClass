"""Question 26: Display student grades based on marks."""


def grade_from_marks(marks: int) -> str:
    if marks >= 90:
        return "A"
    if marks >= 75:
        return "B"
    if marks >= 60:
        return "C"
    if marks >= 40:
        return "D"
    return "F"


def main() -> None:
    marks = 82
    print("Marks:", marks)
    print("Grade:", grade_from_marks(marks))


if __name__ == "__main__":
    main()
