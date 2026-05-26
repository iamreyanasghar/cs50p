import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    parts = ip.strip().split(".")

    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False 

        elif len(part) > 1 and part.startswith("0"):
            return False

        num = int(part)

        if num > 255 or num < 0:
            return False

    return True


if __name__ == "__main__":
    main()

