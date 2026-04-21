"""Question 1: Classify Python data types with examples."""  # Executes this statement.


def main() -> None:  # Defines a function.
    integer_value = 10  # Stores a value in variable(s).
    float_value = 3.14  # Stores a value in variable(s).
    complex_value = 2 + 5j  # Stores a value in variable(s).
    string_value = "Python"  # Stores a value in variable(s).
    list_value = [1, 2, 3]  # Stores a value in variable(s).
    tuple_value = (4, 5, 6)  # Stores a value in variable(s).
    set_value = {7, 8, 9}  # Stores a value in variable(s).
    dictionary_value = {"name": "Asha", "age": 20}  # Stores a value in variable(s).
    boolean_value = True  # Stores a value in variable(s).
    none_value = None  # Stores a value in variable(s).

    print("Numeric: int, float, complex")  # Displays output to the user.
    print(integer_value, type(integer_value))  # Displays output to the user.
    print(float_value, type(float_value))  # Displays output to the user.
    print(complex_value, type(complex_value))  # Displays output to the user.
    print()  # Displays output to the user.
    print("Sequence: str, list, tuple, range")  # Displays output to the user.
    print(string_value, type(string_value))  # Displays output to the user.
    print(list_value, type(list_value))  # Displays output to the user.
    print(tuple_value, type(tuple_value))  # Displays output to the user.
    print(range(3), type(range(3)))  # Displays output to the user.
    print()  # Displays output to the user.
    print("Set types: set, frozenset")  # Displays output to the user.
    print(set_value, type(set_value))  # Displays output to the user.
    print(frozenset(set_value), type(frozenset(set_value)))  # Displays output to the user.
    print()  # Displays output to the user.
    print("Mapping: dict")  # Displays output to the user.
    print(dictionary_value, type(dictionary_value))  # Displays output to the user.
    print()  # Displays output to the user.
    print("Boolean and None")  # Displays output to the user.
    print(boolean_value, type(boolean_value))  # Displays output to the user.
    print(none_value, type(none_value))  # Displays output to the user.


if __name__ == "__main__":  # Checks a condition.
    main()  # Executes this statement.
