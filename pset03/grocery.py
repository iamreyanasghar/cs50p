d = {}

while True:

    try:
        
        item = input()
        
        if item not in d:
            d.update({item: 1})
        
        else:
            d[item] += 1

    except EOFError:
        
        print()

        dictionary = dict(sorted(d.items()))

        for keys in dictionary:
            print(f"{dictionary[keys]} {keys.upper()}")
        
        break

    except KeyError:
        pass

