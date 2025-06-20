from seasons import minutes

def main():
    test_seasons()

def test_seasons():
    assert minutes("2000-12-20") == "Tweleve million, one hundred ninety-nine thousand, six hundred eighty minutes"

if __name__ == "__main__":
    main()
