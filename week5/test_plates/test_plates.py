from plates import is_valid

def main():
    test_validity()

def test_validity():
    assert is_valid("OUTATIME") == False
    assert is_valid("CS50P2") == False
    assert is_valid("NRVOUS") == True
    assert is_valid("CS05") == False
    assert is_valid("H") == False
if __name__ == "__main__":
    main()
