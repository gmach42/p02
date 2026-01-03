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


class GardenManager():
    def __init__(self):
        self.plants = {}
        self.water_level = 5

    def add_plant(self, name, health):
        if health < 0 or health > 10:
            raise PlantError()
        self.plants[name] = health

    def water_plants(self):
        if self.water_level < 3:
            raise WaterError()
        for plant in self.plants:
            self.plants[plant] += 2
        self.water_level -= 3

    def check_plant_health(self):


