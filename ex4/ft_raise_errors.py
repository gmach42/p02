#!/usr/bin/env python3

def check_plant_health(
        plant_name: str,
        water_level: int,
        sunlight_hours: int
        ) -> str:
    """Check the health of a plant and raise errors accordingly."""

    if plant_name == "":
        raise ValueError("Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} "
            "is too high (max 12)"
        )
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    """Test check_plant_health() function with various inputs."""
    print("=== Garden Plant Health Checker ===")

    good_plant = ("rose", 5, 5)
    bad_name = ("", 3, 2)
    bad_water = ("cactus", 15, 6)
    bad_sunlight = ("tulip", 3, 0)

    print("\nTesting good values...")
    try:
        print(check_plant_health(*good_plant))
    except Exception as e:
        print(f"Error: {e}")

    print("\nTesting empty plant name...")
    try:
        print(check_plant_health(*bad_name))
    except Exception as e:
        print(f"Error: {e}")

    print("\nTesting bad water level...")
    try:
        print(check_plant_health(*bad_water))
    except Exception as e:
        print(f"Error: {e}")

    print("\nTesting bad sunlight hours...")
    try:
        print(check_plant_health(*bad_sunlight))
    except Exception as e:
        print(f"Error: {e}")

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
