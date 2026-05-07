user_input = input("Input: ")
r = ""

for c in user_input:
    match c:
        case "a" | "A" | "e" | "E" | "i" | "I" | "o" | "O" | "u" | "U" :
            r += ""

        case _:
            r += c

print("Output:", r)
