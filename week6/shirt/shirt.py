import sys
from PIL import Image, ImageOps

def main():
    try:
        houses = []
        ordered_names = []
        print(sys.argv[1][(len(sys.argv[1]) - 4): len(sys.argv[1])].lower())
        if len(sys.argv) == 3:
            if "jpg" in sys.argv[1].lower() or "png" in sys.argv[1].lower() or "jpeg" in sys.argv[1].lower()  and "jpg" in sys.argv[2].lower() or "png" in sys.argv[2].lower() or "jpeg" in sys.argv[2].lower():
                if sys.argv[1][(len(sys.argv[1]) - 4): len(sys.argv[1])].lower() == sys.argv[2][(len(sys.argv[2]) - 4): len(sys.argv[2])].lower():
                    shirt = Image.open("shirt.png")
                    image = Image.open(sys.argv[1])
                    image = ImageOps.fit(image, shirt.size)
                    image.paste(shirt, shirt)
                    image.save(sys.argv[2])

                else:
                    print("Input and output have different extensions")
                    sys.exit(1)
            else:
                print("Input and output have different extensions")
                sys.exit(1)
        elif len(sys.argv) > 3:
            print("Too many command-line arguments")
            sys.exit(1)
        else:
            print("Too few command-line arguments")
            sys.exit(1)

    except FileNotFoundError:
        print("Could not find the file")
        sys.exit(1)





if __name__ == "__main__":
    main()
