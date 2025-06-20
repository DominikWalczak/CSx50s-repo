import random
def main():
    while True:
        n = input("Level: ")
        if n.isdigit() and int(n) >= 1:
            n = int(n)
            break
    r = random.randint(1, n)
    while True:
        x = input("Guess: ")
        if x.isdigit():
            x = int(x)
            if x == r:
                print("Just right!")
                break
            elif x < r and x >= 0:
                print("Too small!")
            elif x > r and x >= 0:
                print("Too large!")

if __name__ == "__main__":
    main()
