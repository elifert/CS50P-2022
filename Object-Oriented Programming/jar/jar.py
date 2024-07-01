class Jar:
    def __init__(self, capacity=12):
        if capacity > 0:
            self.capacity = capacity
        else:
            raise ValueError
        self.size = 0
        
    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n <= self.capacity:
            self.size += n
        else:
            raise ValueError

    def withdraw(self, n):
        if 0 < self.size - n <= self.capacity:
            self.size -= n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        self._size = size