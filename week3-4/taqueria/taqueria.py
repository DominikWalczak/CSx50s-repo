def main():
    total = 0
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    while True:
        try:
            dish = input("Item: ")
            for d, p in menu.items():
                if dish.lower() == d.lower():
                    total = total + p
                    print(f"Total: ${total:.2f}")
                else:
                    continue
        except EOFError:
            break
if __name__ == "__main__":
    main()
