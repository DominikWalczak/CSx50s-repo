def main():
    r = 0
    while True:
        n = int(input("Insert Coin: "))
        if n == 5 or n == 10 or n == 25:
            if 50 > r+n:
                r+=n
                print(f"Amount Due: {50 - r}")
                continue
            else:
                r+=n
                print(f"Change Owed: {r - 50}")
                break
        else:
            print("Amount Due: 50")

if __name__ == "__main__":
    main()
