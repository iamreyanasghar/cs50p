import operations
import sys

def main():
    while True:
        try:
            print("""
            📌 MAIN MENU:
            ┌─────────────────────────────────────────────────┐
            │ 1. ➕  Add new task                             │
            │ 2. 📋  View all tasks                           │
            │ 3. 🗑️   Remove task                              │
            │ 4. 💾  Save & Exit                              │
            └─────────────────────────────────────────────────┘
            """)

            o = int(input("Operation: "))

            if not valid(o):
                raise ValueError

            match o: 
                case 1:
                    print(operations.add())

                case 2:
                    print(operations.view())

                case 3:
                    print(operations.remove())
                
                case 4:
                    sys.exit("Successfull exit")

        except ValueError:
            print("Invalid operation!")


def valid(n):
    
    if n in [1, 2, 3, 4]:
        return True
    
    else:
        False
    


if __name__ == "__main__":
    main()