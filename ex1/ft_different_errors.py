#!/usr/bin/env python3

def garden_operations(operation: int):
    """Do a couple forbidden operations to demonstrate common errors"""

    # ValueError test:
    if operation == 1:
        int("abc")

    # ZeroDivisionError test:
    if operation == 2:
        545 / 0

    # FileNotFoundError test:
    if operation == 3:
        open("missing.txt", 'r')

    # KeyError test:
    if operation == 4:
        dico = {}
        print(dico["missing_plant"])

    # Multiple error together test:
    if operation == 5:
        int("abc")
        545 / 0
        open("missing.txt", 'r')
        dico = {}
        print(dico["missing_plant"])


def test_error_types():
    """
    Function showing each type of error happening and explains what went wrong
    """

    print("=== Garden Error Types Demo ===")

    print("\nTesting ValueError...")
    try:
        garden_operations(1)
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations(2)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("\nTesting FileNotFoundError...")
    try:
        garden_operations(3)
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    print("\nTesting KeyError...")
    try:
        garden_operations(4)
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    print("\nTesting multiple errors together...")
    try:
        garden_operations(5)
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
