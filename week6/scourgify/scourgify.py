import sys
from tabulate import tabulate
import csv

def main():
    try:
        houses = []
        ordered_names = []
        if len(sys.argv) == 3:
            if ".csv" in sys.argv[1] and ".csv" in sys.argv[2]:
                with open(sys.argv[1], "r") as csvfile:
                    reader = csv.DictReader(csvfile)

                    for line in reader:
                        line2 = line["name"].replace(',','').split()
                        ordered_names.append(line2[1] + " " + line2[0])
                        houses.append(line["house"])
                with open(sys.argv[2], 'w', newline='') as newfile:
                    csvw = csv.writer(newfile)
                    for x in range(len(ordered_names)):
                        csvw.writerow([ordered_names[x], houses[x]])
            else:
                print("Not a CSV file")
                sys.exit(1)
        elif len(sys.argv) > 3:
            print("Too many command-line arguments")
            sys.exit(1)
        else:
            print("Too few command-line arguments")
            sys.exit(1)

    except FileNotFoundError:
        print("Could not read invalid_file.csv")
        sys.exit(1)





if __name__ == "__main__":
    main()
