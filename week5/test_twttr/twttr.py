def main():
    x = shorten(input("Input: "))
    print(f"Output: {x}")

def shorten(n):
    n = n.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "").replace("A", "").replace("E", "").replace("I", "").replace("O", "").replace("U", "")
    return n

if __name__ == "__main__":
    main()
