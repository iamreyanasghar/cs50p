def main():
    user_input = input()
    output = convert(user_input)
    print(output)

def convert(n):
    n = n.replace(":)", "🙂")
    n = n.replace(":(", "🙁")
    return n


main()
