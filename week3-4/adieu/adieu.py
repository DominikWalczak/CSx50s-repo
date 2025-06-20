def main():
    names = []
    text = "Adieu, adieu, to"
    try:
        while True:
            name = input("Name: ")
            if name == "":
                continue
            names.append(name)
    except EOFError:
        for i, name in enumerate(names):
            if name == names[0]:
                text += " " + name
            elif i == 1 and len(names) == 2:
                text += " and " + name
            elif i == len(names) - 1:
                text += ", and " + name
            else:
                text += ", " + name
    print(text)


if __name__ == "__main__":
    main()
