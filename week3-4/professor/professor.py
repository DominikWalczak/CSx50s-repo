import random

def main():
    score = 0
    x = get_level()
    for i in range(10):
        a = generate_integer(x)
        b = generate_integer(x)
        for j in range(3):
            answer = input(f"{a} + {b} = ")
            if answer.isdigit() and int(answer) == a + b:
                score+=1
                break
            print("EEE")
            if j == 2:
                print(f"{a} + {b} = {a + b}")
    print(f"Score: {score}")
def get_level():
    while True:
        try:
            x = int(input("Level: "))
            if x >= 1 and x <= 3:
                break
        except ValueError:
            pass
    return x
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()
