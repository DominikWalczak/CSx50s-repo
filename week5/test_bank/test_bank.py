from bank import value

def main():
    test_hello()

def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hello,") == 0
    assert value("How's it going") == 20
    assert value("Sup bro") == 100
if __name__ == "__main__":
    main()
