import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif sys.argv[1][-3:] != ".py":
    sys.exit("Not a Python file")


try:
    with open(sys.argv[1] , 'r') as file:
        lines = file.readlines()
        n = 0

        for line in lines:
            if line.startswith("#"):
                continue

            elif not line.strip():
                continue

            else:
                n += 1

except FileNotFoundError:
    sys.exit("File does not exist")



print(n)
