def main():
    while True:
        date = update(input("Date: "))
        try:
            print(f"{date[0]}-{date[1]:02}-{date[2]:02}")
            break
        except IndexError:
            pass

def update(d):

    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    b = d
    d = d.replace("/", " ").replace(",", " ")
    dL = d.split()
    if len(dL) == 3 and dL[1].isdigit() and dL[0] in months and "/" not in b and int(dL[1]) < 31 and "," in b:
        dL[0] = months.index(dL[0]) + 1
        return [int(dL[2]), int(dL[0]), int(dL[1])]
    elif len(dL) == 3 and dL[0].isdigit() and dL[1].isdigit() and dL[2].isdigit() and int(dL[2]) >= 0 and int(dL[1]) > 0 and int(dL[0]) > 0 and int(dL[0]) < 13 and int(dL[1]) < 31:
        return [int(dL[2]), int(dL[0]), int(dL[1])]
    else:
        return " "





if __name__ == "__main__":
    main()
