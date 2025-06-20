g = input("Greeting: ")
g_list = g.split()
if g.lower() == "hello" or g_list[0].lower() == "hello" or g_list[0].lower() == "hello,":
    print("$0")
elif g[0].lower() == "h":
    print("$20")
else:
    print("$100")
