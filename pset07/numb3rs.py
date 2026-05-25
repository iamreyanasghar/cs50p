import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    
    pattern = r"^(\d+\.){3}\d+$"

    if re.search(pattern, ip):
        return True

    else:
        return False


if __name__ == "__main__":
    main()

