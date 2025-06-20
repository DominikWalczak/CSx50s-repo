import emoji

def main():
    e = input("Input: ")
    e = emoji.emojize(e, language='en')
    if ":thumbsup:" in e:
        e = e.replace(":thumbsup:", "👍")
    elif ":earth_asia:" in e:
        e = e.replace(":earth_asia:", "🌏")
    print(e)

if __name__ == "__main__":
    main()
