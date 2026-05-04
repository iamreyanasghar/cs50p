greeting = input("Greeting: ")

greeting = greeting.strip().lower()

#if greeting.startswith("hello")   AI way using method
if "hello" in greeting:
    print("$0")

#elif greeting.startswith("h")
elif "h" in greeting[0] and "ello" not in greeting:
    print("$20")

else:
    print("$100")

