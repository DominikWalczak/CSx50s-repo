import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    x = 0
    if "um" in s.lower():
        tab = s.replace(',', ' ').replace('.', ' ').replace('?', ' ').split()
        for t in tab:
            if t.lower() == "um":
                x+=1
        return x
    else:
        return 0

if __name__ == "__main__":
    main()
