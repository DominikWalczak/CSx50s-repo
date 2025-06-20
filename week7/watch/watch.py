import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if "<iframe" in s:
        if "http://www.youtube.com/embed/" in s:
            url = re.search("http://www.youtube.com/embed/([a-zA-Z0-9_-]+)", s)
            return "https://youtu.be/" + url.group(1)
        elif "https://www.youtube.com/embed/" in s:
            url = re.search("https://www.youtube.com/embed/([a-zA-Z0-9_-]+)", s)
            return "https://youtu.be/" + url.group(1)
        elif "https://youtube.com/embed/" in s:
            url = re.search("https://youtube.com/embed/([a-zA-Z0-9_-]+)", s)
            return "https://youtu.be/" + url.group(1)
        else:
            return None
    else:
        return None


if __name__ == "__main__":
    main()
