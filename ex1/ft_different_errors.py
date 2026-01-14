#!/usr/bin/env python3

# def garden_operations(nb1, nb2, filename, key):
#     """Test various error types in garden operations."""
#     result = int(nb1) + int(nb2)
#     division = nb1 / nb2
#     with open(filename, 'r') as file:
#         content = file.read()
#     dict = {"plant": "rose", "tree": "oak"}
#     value = dict[key]
#     _ = result, division, content, value
#     print("All operations completed successfully.")


# def test_error_types():
#     """Test garden_operations() with various error types."""
#     print("=== Garden Error Types Demo ===")
#     print("\nTesting ValueError...")
#     try:
#         garden_operations("ten", 5, "file.txt", "plant")
#     except ValueError as e:
#         print("Caught ValueError:", e)
#     print("\nTesting ZeroDivisionError...")
#     try:
#         garden_operations(10, 0, "file.txt", "plant")
#     except ZeroDivisionError as e:
#         print("Caught ZeroDivisionError:", e)
#     print("\nTesting FileNotFoundError...")
#     try:
#         garden_operations(10, 5, "missing.txt", "plant")
#     except FileNotFoundError as e:
#         print("Caught FileNotFoundError:", e)
#     print("\nTesting KeyError...")
#     try:
#         garden_operations(10, 5, "file.txt", "missing_key")
#     except KeyError as e:
#         print("Caught KeyError:", e)
#     print("\nTesting multiple errors together...")
#     try:
#         garden_operations("ten", 0, "missing.txt", "missing_key")
#     except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
#         print("Caught an error, but program continues!")
#     print("\nAll error types tested successfully!")


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
