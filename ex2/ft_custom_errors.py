#!/usr/bin/env python3

class GardenError(Exception):
    """Base class for garden-related errors."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    """Exception raised when a plant is unhealthy."""
    def __init__(self):
        super().__init__("The tomato plant is wilting!")


class WaterError(GardenError):
    """Exception raised when there is not enough water."""
    def __init__(self):
        super().__init__("Not enough water in the tank!")


def check_garden(plant_health, water_level):
    """Simple function to check garden conditions and raise errors."""
    if plant_health < 5:
        raise PlantError()
    if water_level < 3:
        raise WaterError()


def test_custom_errors():
    """Function demonstrating custom error types."""
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        check_garden(0, 5)
    except PlantError as e:
        print("Caught PlantError:", e)

    print("\nTesting WaterError...")
    try:
        check_garden(10, 0)
    except WaterError as e:
        print("Caught WaterError:", e)

    print("\nTesting catching all garden errors...")
    try:
        check_garden(0, 5)
    except GardenError as e:
        print("Caught a garden error:", e)
    try:
        check_garden(10, 0)
    except GardenError as e:
        print("Caught a garden error:", e)

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
