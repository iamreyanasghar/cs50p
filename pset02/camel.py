def main():
    camelCase = input("camelCase: ")
    snake_case = convert(camelCase)
    print(f"snake_case: {snake_case}")


def convert(s):

    # initializing empty string
    r = ""

    # iterating through every char of string
    for c in s:

        # checks if char is upper
        if c.isupper():

            # replacing upper char with underscore + lower char
            r += "_" + c.lower()

        else:
            # else add that char in result string
            r += c

    return r


main()
