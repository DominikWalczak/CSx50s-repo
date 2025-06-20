from jar import Jar


def test_init():
    assert Jar(12).capacity == 12
    
    assert Jar(10).capacity == 10

    assert Jar(5).capacity == 5

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert int(jar.size) == 0
    jar.deposit(1)
    assert int(jar.size) == 1
    jar.deposit(11)
    assert int(jar.size) == 12


def test_withdraw():
    jar = Jar()
    assert int(jar.size) == 0
    jar.deposit(12)
    jar.withdraw(1)
    assert int(jar.size) == 11
    jar.withdraw(11)
    assert int(jar.size) == 0
