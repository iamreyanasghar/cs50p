import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'<iframe[^>]+src="https?://(?:www\.)?(?:youtube\.com/embed/|youtu\.be/)([^"]+)"'
    matches = re.search(pattern, s)
    
    if matches:
        return f"https://youtu.be/{matches.group(1)}"
    
    else:
        return "None"

if __name__ == "__main__":
    main()

