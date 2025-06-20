from numb3rs import validate

def main():
    test_numb3rs()


def test_numb3rs():
    assert validate("22.22.22.22") == True
    assert validate("255.255.255.255") == True
    assert validate("256.22.22.22") == False
    assert validate("22.287.22.22") == False
    assert validate("100.200.255.140") == True


if __name__ == "__main__":
    main()
