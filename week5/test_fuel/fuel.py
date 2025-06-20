def main():
    while True:
        x = convert()
        y = gauge(x)
        if y != -1:
            break
    print(y)

def convert():
    while True:
        try:
            tank = input("Fraction: ")
            tank = tank.replace("/", " ")
            tankL = tank.split()
            if int(tankL[0]) > int(tankL[1]):
                continue
            elif int(tankL[0]) <= int(tankL[1]):
                return tankL
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
def gauge(tankL):

    try:
        r = round((int(tankL[0])/int(tankL[1]))*100)
        if r <= 1:
            r = "E"
            return r
        elif r >= 99:
            r = "F"
            return r
        r = str(r) + "%"
        return r
    except ZeroDivisionError:
        return -1

if __name__ == "__main__":
    main()
