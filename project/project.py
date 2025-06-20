import sys
def main():
    while True:
        try:
            try:
                try:
                    if not x:
                        x = int(input("Gimme Value: "))
                    if x <= 9223372036854775807 and x >= -9223372036854775808:
                        b = bin(x)
                        h = hex(b)
                        o = oct(b, x)

                        print(f"hexadecimal: {h.strip()}")
                        print(f"decimal: {x}")
                        print(f"octadecimal: {o.strip()}")
                        print(f"binary: {b.strip()}\n\n")
                        x = calc(x)
                    else:
                        raise IndexError
                except NameError:
                    x = int(input("Gimme Value: "))
            except ValueError:
                print("Błąd")
        except IndexError:
            print("You exceeded 9223372036854775807 or -9223372036854775808 with your calculations, program turned off")
            sys.exit(1)
def close():
    while True:
        ans = input("Write yes if you want to close app, if not write no: ").lower()
        if ans == "yes":
            sys.exit(0)
        elif ans == "no":
            return

def calc(n):
    while True:
        x = input("Choose math symbol:\n1. + plus\n2. - minus\n3. * multiplication\n4. / divide\n5. % modulo\n6. +/- negate\nTo stop program write 'stop'\nChoice: ")
        print(n, end="")
        match x.strip():
            case '+':
                n += int(input(" + "))
            case '-':
                n -= int(input(" - "))
            case '*':
                n *= int(input(" * "))
            case '/':
                n /= int(input(" / "))
            case '%':
                n %= int(input(" % "))
            case '+/-':
                n = - n
            case "stop":
                close()
            case _:
                print("Choose one of given symbols")
        print("\n")
        return n
def bin(n):
    result = ""
    if n < 0: #63 to max potęga definująca minus / 62 to max + potęga, pamiętaj
        for i in range(64):
            if i == 0:
                result = result + "1"
            elif n+1 <= -(pow(2, 64-(i+1))) and (-1 != -(pow(2, 64-(i+1))) or n <= -2) :
                l = -(pow(2, 64-(i+1)))
                result = result + "0"
                n = n + pow(2, 64-(i+1))
                if len(result.replace(" ", ""))%4 == 0:
                    result = result + " "
            else:
                result = result + "1"
                if len(result.replace(" ", ""))%4 == 0:
                    result = result + " "
        return result
    elif n == 0:
        return "0"
    else:
        for j in range(64):
            if n >= pow(2, 64-(j+1)):
                result = result + "1"
                n = n - pow(2, 64-(j+1))
            elif n < pow(2, 64-(j+1)) and result != "":
                result = result + "0"


        result1 = result
        for k in range(len(result.replace(" ", ""))):
            if (k + 1) % 4 == 0:
                result1 = result1[:len(result) - k - 1] + " " + result1[len(result) - k - 1:]
    result2 = result1
    if len(result1.replace(" ", ""))%4 != 0:
        result2 = (4 - len(result1.replace(" ", ""))%4) * "0" + result1
    return result2


def hex(m):
    if m == "0":
        return "0"
    hx = ["0", "1", '2', "3", "4", "5", "6", "7", '8', "9", "A", "B", "C", "D", "E", "F"]
    hexa = ""
    tab = m.split()
    for t in tab:
        b = 0
        sum = 0
        for u in t:
            if u == "1":
                sum += pow(2, len(t) - 1 - b)
            b+=1
        hexa = hexa + hx[sum]
    hexa2 = hexa
    for j in range(len(hexa)):
        if (j + 1)%4 == 0:
            hexa2 = hexa2[:len(hexa) - j - 1] + " " + hexa2[len(hexa) - j - 1:]
    return hexa2


def oct(k, p):# błąd w octa jest usuwa 1 z liczb 12 itd. zweryfikuj to jutro
    if p == 0:
        return "0"
    octa = ""
    k = k.replace(" ", "")
    k1 = k
    for i in range(len(k)):
        if (i + 1)%3 == 0:
            k1 = k1[:len(k) - i - 1] + " " + k1[len(k) - i - 1:]
    tab = k1.split()
    for t in tab:
        re = 0
        if len(t) == 3:
            if t[0] == "1":
                re = re + 4
            if t[1] == "1":
                re = re + 2
            if t[2] == "1":
                re = re + 1
        elif len(t) == 2:
            if t[0] == "1":
                re = re + 2
            if t[1] == "1":
                re = re + 1
        elif len(t) == 1:
            if t[0] == "1":
                re = re + 1
        octa = octa + str(re)
    octa2 = octa
    for j in range(len(octa)):
        if (j + 1)%3 == 0:
            octa2 = octa2[:len(octa) - j - 1] + " " + octa2[len(octa) - j - 1:]
    if octa2[0] == "0":
        octa2 = octa2[1:len(octa2)]
    elif octa2[1] == "0":
        octa2 = octa2[2:len(octa2)]
    return octa2
if __name__ == "__main__":
    main()
