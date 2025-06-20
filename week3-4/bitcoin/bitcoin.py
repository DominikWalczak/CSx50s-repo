import sys
import requests

def main():
    try:
        x = float(sys.argv[1])
        price = bp()
        print(f"${price*x:,.4f}")
    except ValueError and IndexError:
        if IndexError:
            print("Missing command-line argument")
            sys.exit(1)
        else:
            print("Command-line argument is not a number")
            sys.exit(1)


def bp():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        d = response.json()
        r = d["bpi"]["USD"]["rate_float"]
        return r
    except requests.RequestException:
        sys.exit(1)

if __name__ == "__main__":
    main()
