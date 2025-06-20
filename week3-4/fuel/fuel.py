def main():
    while True:
        try:
            tank = input("Fraction: ")
            tank = tank.replace("/", " ")
            tankL = tank.split()
            if int(tankL[0]) > int(tankL[1]):
                continue

            r = round((int(tankL[0])/int(tankL[1]))*100)
            if r <= 1:
                r = "E"
                break
            elif r >= 99:
                r = "F"
                break
            r = str(r) + "%"
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
    print(r)

if __name__ == "__main__":
    main()
