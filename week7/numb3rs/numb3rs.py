
def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    x = 0
    tab = ip.replace('.', ' ').split()
    if len(tab) == 4:
        for t in tab:
            try:
                if int(t) <= 255:
                    x += 1
                    if x == 4:
                        return True
            except ValueError:
                pass

    else:
        return False
    return False

if __name__ == "__main__":
    main()
