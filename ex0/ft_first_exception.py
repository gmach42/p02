#!/usr/bin/env python3

def check_temperature(temp_str):
    """Check if the temperature is within a valid range and is an integer."""
    try:
        temp_int = int(temp_str)
    except ValueError:
        raise ValueError(f"'{temp_str}' is not a valid number")
    if 0 < temp_int < 40:
        return (f"Temperature {temp_int}°C is perfect for plants!")
    elif temp_int <= 0:
        raise ValueError(f"{temp_int}°C is too cold! (min 0°C)")
    else:
        raise ValueError(f"{temp_int}°C is too hot! (max 40°C)")


def test_temperature_input():
    """Test check_temperature() with various inputs and run despite errors."""
    print("=== Gardent Temperature Checker ===")
    temps = ["25", "abc", "100", "-50"]
    for temp in temps:
        print(f"\nTesting temperature: {temp}")
        try:
            print(check_temperature(temp))
        except ValueError as e:
            print(f"Error: {e}")
    print("\nAll tests completed - program didn't crash!")


test_temperature_input()
