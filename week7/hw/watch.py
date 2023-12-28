import sys
import re

def main():
    print(parse(input("HTML:")))


def parse(s):
    if matches := re.match(r'.*?src="https?\://(?:www\.)?youtube\.com(?:/embed)?/(\w+)".*?',s):
        ss = matches.group(1)
        return f"https://youtu.be/{ss}"
    else :
        return None
if __name__ == "__main__":
    main()
