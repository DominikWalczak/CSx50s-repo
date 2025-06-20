from um import count

def main():
    test_um()





def test_um():
    assert count("um, what's up") == 1
    assert count("um") == 1
    assert count("umm") == 0
    assert count("yum") == 0
    assert count("Um") == 1
    assert count("um, hello um") == 2



if __name__ == "__main__":
    main()
