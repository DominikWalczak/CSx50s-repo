from fuel import convert, gauge

def main():
    test_validity()

def test_validity():
    assert gauge(convert("1/2")) == '50%'
    assert gauge(convert("3/4")) == '75%'
    assert gauge(convert("2/3")) == '67%'
    assert gauge(convert("99/100")) == 'F'
    assert gauge(convert("1/100")) == 'E'
if __name__ == "__main__":
    main()
