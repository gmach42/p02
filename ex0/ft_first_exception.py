#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int:
    """Function which return a temp only when a valid input is send"""
    try:
        temp = int(temp_str)
        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        else:
            return temp
    except Exception:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input():
    """
    Test different inputs to demonstrate that the bad data is filtered out
    """
    print("=== Garden Temperature Checker ===")
    test_values = ["25", "abc", "100", "-50"]
    for value in test_values:
        print(f"\nTesting temperature: {value}")
        temp = check_temperature(value)
        if temp:
            print(f"Temperature {temp}°C is perfect for plants!")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
