import sys
from tabulate import tabulate
import csv

def main():
    try:
        if len(sys.argv) == 2:
            if ".csv" in sys.argv[1]:
                with open(sys.argv[1], "r") as csvfile:
                    reader = csv.reader(csvfile, delimiter=',')
                    headers = next(reader)
                    rows = [row for row in reader]
                    print(tabulate(rows, headers, tablefmt="grid"))
            else:
                print("Not a CSV file")
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
