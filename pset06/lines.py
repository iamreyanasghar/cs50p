import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif sys.argv[-3:] != ".py":
    sys.exit("Not a Python file")

else:
    file_name = sys.argv[1]

    try:
        with open(file_name) as file:
            print("File found and read successfully!")

    except FileNotFoundError:
        sys.exit("File does not exist")
