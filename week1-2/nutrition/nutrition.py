class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories


def main():
    x = search(input("Item: "))
    print(x)

def search(f):
    fruits = [
        Fruit(name='Apple', calories=130),
        Fruit(name='Avocado', calories=50),
        Fruit(name='Banana', calories=110),
        Fruit(name='Cantaloupe', calories=50),
        Fruit(name='Grapefruit', calories=60),
        Fruit(name='Grapes', calories=90),
        Fruit(name='Honeydew Melon', calories=50),
        Fruit(name='Kiwifruit', calories=90),
        Fruit(name='Lemon', calories=15),
        Fruit(name='Lime', calories=20),
        Fruit(name='Nectarine', calories=60),
        Fruit(name='Orange', calories=80),
        Fruit(name='Peach', calories=60),
        Fruit(name='Pear', calories=100),
        Fruit(name='Pineapple', calories=50),
        Fruit(name='Plums', calories=70),
        Fruit(name='Strawberries', calories=50),
        Fruit(name='Sweet Cherries', calories=100),
        Fruit(name='Tangerine', calories=50),
        Fruit(name='Watermelon', calories=80),
    ]
    for fruit in fruits:
        if fruit.name.lower() == f.lower():
            f = fruit.calories
            return f
    f = ""
    return f

if __name__ == "__main__":
    main()
