import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    parts = re.findall(r'\D+|\d+', s)
    if len(parts[0]) >= 2:
        if len(parts) >= 2 and len(s) >= 2 and len(s) <= 6:
            if parts[1].isdigit() and parts[1][0] != "0" and len(parts) == 2:
                return True

        elif s.isalpha() and len(s) >= 2 and len(s) <= 6:
            return True 

    else:
        return False


main()

