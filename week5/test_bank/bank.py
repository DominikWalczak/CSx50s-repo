def main():
    g = hello(input("Greeting: "))

def value(g):
    g_list = g.split()
    if g.lower() == "hello" or g_list[0].lower() == "hello" or g_list[0].lower() == "hello,":
        return 0
    elif g[0].lower() == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
