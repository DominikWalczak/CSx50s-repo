import sys


def main():
    try:
        if len(sys.argv) == 2:
            x = 0
            if ".py" in sys.argv[1]:
                with open(sys.argv[1], "r") as file:
                    for line in file:
                        if line.strip() and "#" not in line:
                            x+=1
                print(x)
            else:
                print("File name needs to end with .py")
                sys.exit(1)
        elif len(sys.argv) > 2:
            print("Too many command-line arguments")
            sys.exit(1)
        else:
            print("Too few command-line arguments")
            sys.exit(1)

    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)





if __name__ == "__main__":
    main()
