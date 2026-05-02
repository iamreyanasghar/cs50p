ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

answer = ans.lower().strip().replace(" ", "-")

match answer:
    case "42" | "forty-two":
        print("Yes")
    case _:
        print("No")

