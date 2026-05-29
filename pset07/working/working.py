import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        start, end = s.split(" to ")

        h1, *m1 = start.split()[0].split(":")
        p1 = start.split()[1]

        h2, *m2 = end.split()[0].split(":")
        p2 = end.split()[1]

        if m1 and len(m1[0]) != 2:
            raise ValueError

        if m2 and len(m2[0]) != 2:
            raise ValueError

        m1 = int(m1[0]) if m1 else 0
        m2 = int(m2[0]) if m2 else 0

        h1 = int(h1)
        h2 = int(h2)

        if not (1 <= h1 <= 12 and 1 <= h2 <= 12):
            raise ValueError

        if not (0 <= m1 <= 59 and 0 <= m2 <= 59):
            raise ValueError

        if p1 == "AM" and h1 == 12:
            h1 = 0
        elif p1 == "PM" and h1 != 12:
            h1 += 12
        elif p1 not in ["AM", "PM"]:
            raise ValueError

        if p2 == "AM" and h2 == 12:
            h2 = 0
        elif p2 == "PM" and h2 != 12:
            h2 += 12
        elif p2 not in ["AM", "PM"]:
            raise ValueError

        return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"

    except:
        raise ValueError


if __name__ == "__main__":
    main()

