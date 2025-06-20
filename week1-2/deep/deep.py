def main():
    ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")

    if ans.replace(" ", "") == "42" or ans.lower() == "forty two" or ans.lower() == "forty-two":
        print("Yes")
    else:
        print("No")

main()
