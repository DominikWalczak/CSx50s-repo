def main():
    dictL = {}
    while True:
        try:
            g = input("")
            if g in dictL:
                dictL[g] = int(dictL[g]) + 1
            else:
                dictL[g] = 1
        except EOFError:
            break

    sdictL = sorted(dictL)

    for food in sdictL:
        value = dictL[food]
        print(f"{value} {food.upper()}")

if __name__ == "__main__":
    main()
