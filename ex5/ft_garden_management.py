#!/usr/bin/env python3

class GardenError(Exception):
    """Base class for garden-related errors."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class WaterError(GardenError):
    """Exception raised when the water level is not good"""
    def __init__(self, water_level: int):
        if water_level < 1:
            self.message = f"Water level {water_level} is too low (min 1)"
        elif water_level > 10:
            self.message = f"Water level {water_level} is too high (max 10)"
        else:
            self.message = "This shouldn't have raised a WaterError..."
        super().__init__(self.message)


class SunlightError(GardenError):
    """Exception raised when the sunlight level is not good"""
    def __init__(self, sun_level: int):
        if sun_level < 2:
            self.message = f"{sun_level} sunlight hours is too low (min 2)"
        elif sun_level > 12:
            self.message = f"{sun_level} sunlight hours is too high (max 12)"
        else:
            self.message = "This shouldn't have raised a SunlightError..."
        super().__init__(self.message)


class WaterTankError(GardenError):
    """Exception raised when the water in the tank is too low"""
    def __init__(self):
        self.message = "Not enough water in the tank"
        super().__init__(self.message)


class Plant:
    """
    Simple plant class with a name, a level of water and sunlight exposure
    """
    def __init__(self, name: str, water: int, sunlight: int):
        self.name = name
        self.water = water
        self.sunlight = sunlight


class GardenManager:
    """A class to manage a garden with expansive error handling"""
    def __init__(self, name: str, initial_water: int = 5):
        self.name = name
        self.tank_water = initial_water
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant):
        try:
            if not plant.name:
                raise ValueError("Plant name cannot be empty!")
            if not isinstance(plant.name, str):
                raise ValueError(f"{plant.name} is an invalid plant name!")
            self.plants.append(plant)
        except Exception as e:
            print(f"Error adding plant: {e}")
        else:
            print(f"Added {plant.name} successfully")

    def remove_plant(self, name: str):
        try:
            for plant in self.plants:
                if plant.name == name:
                    self.plants.remove(plant)
        except ValueError:
            print(f"no {name} is planted in the garden...")
        else:
            print(f"{name} removed successfully")

    def check_plants_health(self) -> str:
        """
        Check the plant's health in the garden and raise errors accordingly.
        """
        try:
            for plant in self.plants:
                if plant.water < 1:
                    raise WaterError(plant.water)
                if plant.water > 10:
                    raise WaterError(plant.water)
                if plant.sunlight < 2:
                    raise SunlightError(plant.sunlight)
                if plant.sunlight > 12:
                    raise SunlightError(plant.sunlight)
                print(
                    f"{plant.name} (water: {plant.water}, "
                    f"sun: {plant.sunlight}) is healthy!"
                )
        except Exception as e:
            print(f"{type(e).__name__} checking {plant.name}: {e}")
        else:
            print("All plants are healthy!")

    def water_plants(self):
        """
        Simulate watering plants in the garden, raise exception for
        invalid inputs and always closes the watering system!
        """
        try:
            print("Opening watering system")
            for plant in self.plants:
                if not isinstance(plant.name, str):
                    raise ValueError("invalid plant")
                print(f"Watering {plant.name} - success")

        except Exception as e:
            print(f"Error: Cannot water {plant.name} - {e}!")

        else:
            print("Watering completed successfully!")

        finally:
            print("Closing watering system (cleanup)")

    def check_water_tank(self):
        if self.tank_water < 10:
            raise WaterTankError()
        else:
            print("The tank has enough water!")


def test_garden_management():
    """Test the GardenManager to see if handles input correctly..."""
    print("=== Garden Management System ===")

    garden = GardenManager("garden")

    print("\nAdding plants to garden...")
    # (plant_name, water_level, sunlight_hour)
    tomato = Plant("tomato", 5, 8)
    lettuce = Plant("lettuce", 15, 3)
    sunflower = Plant("sunflower", 6, 50)
    empty_plant = Plant("", 5, 8)
    invalid_plant = Plant(123, 5, 8)

    plants = [tomato, lettuce, sunflower, empty_plant, invalid_plant]
    for plant in plants:
        garden.add_plant(plant)

    print("\nWatering plants...")
    garden.water_plants()

    print("\nChecking plants health...")
    garden.check_plants_health()

    # Removing the lettuce to test the SunlightError with the sunflower
    print("\nRemoving the lacking lettuce...")
    garden.remove_plant("lettuce")
    print("\nChecking plants health once more...")
    garden.check_plants_health()

    print("\nTesting error recovery...")
    try:
        garden.check_water_tank()
        garden.check_plants_health()
        garden.add_plant(empty_plant)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    else:
        print("Everything is perfect in my garden!")
    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
