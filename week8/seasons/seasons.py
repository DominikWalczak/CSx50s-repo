from datetime import date, datetime
import sys
import inflect

def main():
    s = minutes(input("Date of birth: "))
    if s == "ValueError":
        sys.exit(1)

def minutes(s):
    try:
        s = date.fromisoformat(s)
        x = date.today()
        n = datetime.combine(x, datetime.min.time()) - datetime.combine(s, datetime.min.time())
        p = int(n.total_seconds() / 60)
        min = inflect.engine()
        words = min.number_to_words(p)
        words = words.capitalize().replace(" and", '')
        print(f"{words} minutes")

    except ValueError:
        return "ValueError"
if __name__ == "__main__":
    main()
