def main():
    user_input = input("Input: ")
    result = shorten(user_input)
    print(result)

def shorten(word):
    r = ''

    for c in word:
        match c:
            case "a" | "A" | "e" | "E" | "i" | "I" | "o" | "O" | "u" | "U" :
                r += ""

            case _:
                r += c

    return r

if __name__ == "__main__":
    main()
