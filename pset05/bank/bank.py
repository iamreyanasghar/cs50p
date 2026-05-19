def main():
    greetings = input("Greeting: ")
    score = value(greetings)
    print(f"${score}")


def value(greeting):

    greet = greeting.lower()

    if greet.startswith("hello"):
        return 0

    elif greet.startswith("h"):
        return 20

    else:
        return 100


if __name__ == "__main__":
    main()
