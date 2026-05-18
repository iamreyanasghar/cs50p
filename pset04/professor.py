import random


def main():
    level = get_level()

    score = 0

    # ask question 10 times
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        ans = fails = 0
        
        # check whether answer given is correct or not
        while fails < 3:
            try:
                ans = int(input(f"{x} + {y} = "))
                
                if ans == answer:
                    score += 1
                    break
                
                else:
                    print("EEE")
                    fails += 1

            except ValueError:
                print("EEE")
                fails += 1 

        if fails == 3:
            print(f"{x} + {y} = {x + y}")

    print(f"Score: {score}")


# take input as 1, 2, 3 else continue loop 
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level

        except ValueError:
            pass


# generate int of ( level ) number of digits
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)

    elif level == 2:
        return random.randint(10, 99)

    elif level == 3:
        return random.randint(100, 999)
    
    else:
        raise ValueError

if __name__ == "__main__":
    main()

