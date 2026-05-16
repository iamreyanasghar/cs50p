adieu = "Adieu, adieu, to "

while True:
    try:
        names = []
        while True:
            name = input("Name: ")
            names.append(name)

            if len(names) > 1:
                output = adieu + names[0]
                for i in range(1, len(names)):
                    output += ", " + names[i]

            else:
                output = adieu + name

    except EOFError:
        if len(names) == 2:
            index = output.rfind(",")
            result = output[:index] + " and" + output[index+1:]
        
        elif len(names) > 2:
            index = output.rfind(",")
            result = output[:index] + ", and" + output[index+1:]
        
        else:
            result = output

        print(f"\n{result}")
        break
