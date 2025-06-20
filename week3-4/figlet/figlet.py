from pyfiglet import Figlet
import sys
import random

def main():
    f = Figlet()
    fonts = f.getFonts()
    if len(sys.argv) == 1:
        s = input("Input: ")
        rfont = random.choice(fonts)
        f2 = Figlet(font=rfont)
        f2 = f2.renderText(s)
        print(f"Output: {f2}")
    elif len(sys.argv) == 3 and sys.argv[2] in fonts:
        if sys.argv[1] == '-f' or sys.argv[1] == '--font':
            s = input("Input: ")
            f2 = Figlet(font=sys.argv[2])
            f2 = f2.renderText(s)
            print(f"Output: {f2}")
        else:
            print("Invalid usage")
            sys.exit(1)
    else:
        print("Invalid usage")
        sys.exit(1)

if __name__ == "__main__":
    main()
