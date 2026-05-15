adieu = "Adieu, adieu, to "

while True:
    try:
        names = []
        while True:
            name = input("Name: ")
            names.append(name)

            if len(names) == 1:
                output = adieu + names[0]
            else:
                output = adieu + name
                for i in range(len(names)):
                    output += ", " + names[i]

        print()

    except EOFError:
        print(output)
        break
