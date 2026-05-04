def main():
    time = input("What time is it? ")
    num = convert(time)

    if num >= 7 and num <= 8:
        print("breakfast time")

    elif num >= 12 and num <= 13:
        print("lunch time")

    elif num >= 18 and num <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes) / 60
    ans = float(hours) + float(minutes)
    return ans

if __name__ == "__main__":
    main()

