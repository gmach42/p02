#!/usr/bin/env python3

class GardenError(Exception):
    """Base class for garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised when a plant is unhealthy."""
    def __init__(self):
        super().__init__("The tomato plant is wilting!")


class WaterError(GardenError):
    """Exception raised when there is not enough water."""
    def __init__(self):
        super().__init__("Not enough water in the tank!")


def check_garden(water_level, plant_health):
    if plant_health < 5:
        raise PlantError()
    if water_level < 3:
        raise WaterError()


print("=== Custom Garden Errors Demo ===")
print("\nTesting PlantError...")
try:
    check_garden(5, 0)
except PlantError as e:
    print("Caught PlantError:", e)


print("\nTesting WaterError...")
try:
    check_garden(0, 10)
except WaterError as e:
    print("Caught WaterError:", e)


print("\nTesting catching all garden errors...")
try:
    check_garden(5, 0)
except GardenError as e:
    print("Caught a garden error:", e)
try:
    check_garden(0, 10)
except GardenError as e:
    print("Caught a garden error:", e)
