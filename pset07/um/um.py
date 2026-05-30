import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
        
    ans = s.lower().split(" ")
    count = 0
    pattern = r"^(?:\.|,| |\?)*um(?:\.|,| |\?)*$"
    
    for i in range(len(ans)):
        matches = re.search(pattern, ans[i])
        if matches:
            count += 1
    
    return count


if __name__ == "__main__":
    main()

