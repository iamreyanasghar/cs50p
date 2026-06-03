class Jar:
    def __init__(self, capacity=12):

        if capacity < 0:
            raise ValueError("Negative capacity")

        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return f"🍪" * self.size


    def deposit(self, n):

        if self.size + n > self.capacity:
            raise ValueError("Capacity exeeded")

        self._size += n


    def withdraw(self, n):

        if n > self.size:
            raise ValueError("Not enough cookies to withdraw")

        self._size -= n
    

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

