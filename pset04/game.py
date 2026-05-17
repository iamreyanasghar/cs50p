from random import randint
import sys

def main():

    level = get_int("Level: ")
    
    random_int = randint(1, level)
    
    while True:
        guess = get_int("Guess: ")

        if guess > random_int:
            print("Too large!")

        elif guess < random_int:
            print("Too small!")

        else:
            sys.exit("Just right!")


def get_int(prompt):
    while True:
        try:
            n =  int(input(prompt))

            if n >= 1:
                return n 

        except ValueError:
            pass


if __name__ == "__main__":
    main()
