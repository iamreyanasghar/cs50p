expression = input("Expression: ")

x, z, y = expression.split(" ")

x = int(x)
y = int(y)

if z == "+":
    print(float(x + y))

elif z == "-":
    print(float(x - y))

elif z == "*":
    print(float(x * y))

elif z == "/":
    print(float(x / y))

