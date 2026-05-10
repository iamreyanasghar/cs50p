while True:
    fraction = input("Fraction: ")
    try:
        x_str, y_str = fraction.split("/")
        x = int(x_str)
        y = int(y_str)
        
        if x > y and y == 0:
            continue

    except (ValueError, ZeroDivisionError):
        continue

    break

z = round((x / y) * 100)

if z <= 1:
    print("E")

elif z >= 99:
    print("F")

else:
    print(f"{z}%")
