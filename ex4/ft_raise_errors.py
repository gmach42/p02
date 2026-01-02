#!/usr/bin/env python3

def check_plant_health(plant_name, water_level, sunlight_hours):
    """Check the health of a plant and raise errors accordingly."""
    if plant_name == "":
        raise ValueError("Plant name cannot be empty!")
    if water_level < 2:
        raise ValueError(f"Water level {water_level} is too low (min 2)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours}"
            " is too high (max 12)"
        )
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    """Test check_plant_health() function with various inputs."""
    print("=== Garden Plant Health Checker ===")
    plant1 = ("rose", 5, 5)
    plant2 = ("", 3, 2)
    plant3 = ("cactus", 15, 6)
    plant4 = ("tulip", 3, 0)

    print("\nTesting good values...")
    try:
        print(check_plant_health(*plant1))
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTesting empty plant name...")
    try:
        print(check_plant_health(*plant2))
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTesting bad water level...")
    try:
        print(check_plant_health(*plant3))
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTesting bad sunlight hours...")
    try:
        print(check_plant_health(*plant4))
    except ValueError as e:
        print(f"Error: {e}")
    print("\nAll error raising tests completed!")


test_plant_checks()
