def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    x = 0
    y = 0
    a = ""
    b = ""

    for word in s:
        x+=1
        if len(s) <= 6 and len(s) >= 2 and word != "," and word != "." and word != " ":
            if x <= 2 and word.isalpha() or y >= 2:
                y+=1
                if word.isdigit() and False == a.isalpha():
                    b = word
                    if y == len(s):
                        return True
                elif word.isalpha() and False == b.isdigit():
                    a = word
                    if y == len(s):
                        return True
                else:
                    return False
            else:
                return False
        else:
            return False

if __name__ == "__main__":
    main()
