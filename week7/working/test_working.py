from working import convert
import sys
def main():

    test_working()
    sys.exit(0)

def test_working():
    assert convert("9 AM to 12 PM") == "09:00 to 12:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("09:05 AM to 12:59 PM") == "09:05 to 12:59"


if __name__ == "__main__":
    main()
