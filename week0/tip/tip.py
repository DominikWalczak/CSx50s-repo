def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.replace("$", "")
    if d.replace(".", "").isdigit():
        d = float(d)
        return d
    else:
        print("Number need to be given, only")
        return 1
def percent_to_float(p):
    p = p.replace("%", "")
    if p.isdigit():
        p = float(p)
        return p/100
    else:
        print("Number need to be given, only")
        return 1


main()
