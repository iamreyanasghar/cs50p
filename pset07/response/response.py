import validators

def main():
    user_input = input("What's your email address? ")
    print(valid(user_input))


def valid(s):

    if validators.email(s):
        return "Valid"

    else: 
        return "Invalid"


if __name__ == "__main__":
    main()
