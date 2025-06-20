words = input("The program converts given faces to emotes, got any to change? ")

wordL = words.split()

for i in range(len(wordL)):
    if wordL[i] == ":)":
        wordL[i] = "🙂"
    elif wordL[i] == ":(":
        wordL[i] = "🙁"

words = ' '.join(wordL)
print(f"Switched emojis look like: {words}")
