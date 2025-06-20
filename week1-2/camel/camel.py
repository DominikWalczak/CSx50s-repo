def main():
    n = convert(input("camelCase: "))
    print(n)

def convert(x):
    y = 0
    a = ""
    for char in x:
        if char.isalpha() and char.isupper():
            a += " " + x[y]
        else:
            a += x[y]
        y+=1
        a = a.replace(" ", "_").lower()
    return a


if __name__ == "__main__":
    main()
