import sys
import csv
from tabulate import tabulate


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif sys.argv[1][-4:] != ".csv":
    sys.exit("Not a Python file")

try:
    pizza = []
    name = sys.argv[1]
    with open(name) as file:
        reader = list(csv.reader(file))
        for row in reader:
            pizza.append(row)

        table = tabulate(pizza, headers="firstrow", tablefmt="grid")

except FileNotFoundError:
    sys.exit("File does not exist")

print(table)

