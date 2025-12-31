def garden_operations(nb1, nb2, filename, key):
    try:
        result = int(nb1) + int(nb2)
        division = nb1 / nb2
        with open(filename, 'r') as file:
            content = file.read()
        dict = {"plant": "rose", "tree": "oak"}
        value = dict[key]
        print("All operations completed successfully.")

    except ValueError as ve:
        print("Caught ValueError:", ve)

    except ZeroDivisionError as zde:
        print("Caught ZeroDivisionError:", zde)

    except FileNotFoundError as fnfe:
        print("Caught FileNotFoundError:", fnfe)

    except KeyError as ke:
        print("Caught KeyError:", ke)


def test_error_types():
    print("=== Garden Error Types Demo ===")
    print("Testing ValueError...")
    garden_operations("ten", 5, "file.txt", "plant")
    print("\nTesting ZeroDivisionError...")
    garden_operations(10, 0, "file.txt", "plant")
    print("\nTesting FileNotFoundError...")
    garden_operations(10, 5, "missing.txt", "plant")
    print("\nTesting KeyError...")
    garden_operations(10, 5, "file.txt", "missing_key")
    print("\nTesting multiple errors together...")
    garden_operations("ten", 0, "missing.txt", "missing_key")
    print("\nAll error types tested successfully!")
    print("\nTesting no errors...")
    garden_operations(10, 5, "file.txt", "plant")

test_error_types()
