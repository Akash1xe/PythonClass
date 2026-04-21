"""Case study 2: Library book details with data types."""  # Executes this statement.


def main() -> None:  # Defines a function.
    title = input("Enter book title: ")  # Reads input from the user.
    author = input("Enter author name: ")  # Reads input from the user.
    price = float(input("Enter price: "))  # Stores a value in variable(s).

    print("Book details:")  # Displays output to the user.
    print("Title:", title, type(title))  # Displays output to the user.
    print("Author:", author, type(author))  # Displays output to the user.
    print("Price:", price, type(price))  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
