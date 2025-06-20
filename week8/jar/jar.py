class Jar:

    def __init__(self, capacity=12):
        self._size = 0
        if int(capacity) < 0:
            raise ValueError("capacity is negative")
        self._capacity = capacity
    def __str__(self):
        return int(self._size) * '🍪'

    def deposit(self, n):
        if int(n) < 0:
            raise ValueError("You cannnot add negative amount of cookies")
        elif  self._size + int(n) > self._capacity:
            raise ValueError("You reached capacity of the jar")
        self._size += int(n)

    def withdraw(self, n):
        if int(n) < 0:
            raise ValueError("You cannnot take negative amount of cookies")
        elif  self._size - int(n) < 0:
            raise ValueError(f"You cannot take {n} cookies from { self._size}")
        self._size -= int(n)

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        print(capacity)
        if int(capacity) < 0:
            raise ValueError("capacity is negative")
        self._capacity = capacity
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        if int(size) < 0:
            print(size)
            raise ValueError("size is negative")
        elif int(size) > self._capacity:
            raise ValueError("size is above 12")
        self._size = size


def main():
    jar = get_jar()
    print(jar.capacity)
    while True:
        jar.withdraw(input("liczba: "))
        print(jar.size)
        jar.deposit(input("liczba2: "))
        print(jar.size)


def get_jar():
    jar = Jar(input("liczba3: "))
    return jar

if __name__ == "__main__":
    main()
