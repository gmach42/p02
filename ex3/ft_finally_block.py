#!/usr/bin/python3

def water_plants(plant_list):
    try:
        pass
    except:
        pass
    finally:
        print("Closing watering system (cleanup)")







print("=== Garden Watering System ===")
print("\nTesting normal watering...")
plant_list = {"tomato", "lettuce", "carrots"}
water_plants(plant_list)
print("\nTesting with error...")
plant_list = {}
water_plants(plant_list)
