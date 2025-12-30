def check_temperature(temp_str):
    try:
        temp_int = int(temp_str)
        if 0 < temp_int < 40:
            return temp_int
        elif temp_int <= 0:
            return "Too cold!"
        else:
            return "Too hot!"
    except ValueError:
        print("your input is not a number")


print(check_temperature("25"))
print(check_temperature("45"))
print(check_temperature("abc"))
