#!/usr/bin/env python3

def water_plants(plant_list):
    """Simulate watering plants in a garden."""
    print("Opening watering system")
    for plant in plant_list:
        print(f"Watering {plant}...")


def test_watering_system(plant_list):
    """Test the watering system with exception handling."""
    try:
        water_plants(plant_list)
    except Exception as e:
        print(f"Error: Cannot water {plant_list} -", e)
    finally:
        print("Closing watering system (cleanup)")


print("=== Garden Watering System ===")
print("\nTesting normal watering...")
plant_list = {"tomato", "lettuce", "carrots"}
test_watering_system(plant_list)
print("\nTesting with error...")
plant_list = {}
test_watering_system(plant_list)
