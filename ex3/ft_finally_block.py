#!/usr/bin/env python3


def water_plants(plant_list: list[str]):
    """
    Simulate watering plants in a garden, raise exception for invalid input
    and always closes the watering system!
    """
    try:
        print("Opening watering system")
        for plant in plant_list:
            if not isinstance(plant, str):
                raise ValueError("invalid plant")
            print(f"Watering {plant}")

    except Exception as e:
        print(f"Error: Cannot water {plant} - {e}!")

    else:
        print("Watering completed successfully!")

    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """
    Test the watering system with valid and invalid inputs
    and always cleanup!
    """
    print("=== Garden Watering System ===")

    print("\nTesting normal watering...")
    valid_list = ["tomato", "lettuce", "carrots"]
    water_plants(valid_list)

    print("\nTesting with error...")
    error_list = ["tomato", None, "carrots"]
    water_plants(error_list)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
