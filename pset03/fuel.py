while True:
    fraction = input("Fraction: ")
    try:
        x_str, y_str = fraction.split("/")
        x = int(x_str)
        y = int(y_str)
        
        if x > y and y == 0:
            continue
        
        z = round((x / y) * 100)

        if z <= 1 and z >= 0:
            print("E")

        elif z >= 99 and z <= 100:
            print("F")

        elif z < 0 or z > 100:
            continue       

        else:
            print(f"{z}%")

    except (ValueError, ZeroDivisionError):
        pass

    else:
        break
