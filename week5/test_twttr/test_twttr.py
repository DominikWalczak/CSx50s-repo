from twttr import shorten

def main():
    test_convert()

def test_convert():
    assert shorten("twitter") == 'twttr'
    assert shorten("TWITTER") == 'TWTTR'
    assert shorten("TwItTeR") == 'TwtTR'
    assert shorten("312321") == '312321'
    assert shorten("}||:|}||") == '}||:|}||'
if __name__ == "__main__":
    main()
