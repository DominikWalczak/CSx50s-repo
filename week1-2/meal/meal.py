def main():
    time = convert(input("What time is it? "))
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")

def convert(time):
        time = time.replace(":", " ")
        timeL = time.split()
        n = float(timeL[0])
        y = float(timeL[1])/60
        return n + y
if __name__ == "__main__":
    main()
