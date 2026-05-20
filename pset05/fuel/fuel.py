def main():
    while True:
        fraction = input("Fraction: ")
        
        try:
            percentage = convert(fraction)
            print(guage(percentage))
            break
        except (ZeroDivisionError, ValueError):
            pass

def convert(fraction):
    
    x_str, y_str = fraction.split("/")
    x = int(x_str)
    y = int(y_str)
        

    if x < 0 or y <= 0 or x > y:
        raise ValueError
            
    return round((x / y) * 100)
    

def guage(percentage):
    if percentage <= 1:
        return "E"

    elif percentage >= 99:
        return "F"

    else:
        return (f"{percentage}%")


if __name__ == "__main__":
    main()
