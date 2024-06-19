class ArrayDeque:
    """Double-ended queue implemented using a circular array"""

    def __init__(self):
        """Constructor, O(1)"""
        self._capacity = 10
        self._deque = [None] * self._capacity
        self._size = 0
        self._next_first = 4
        self._next_last = 5

    def size(self) -> int:
        """Return the number of elements in the deque, O(1)"""
        return self._size

    def is_empty(self) -> bool:
        """Check if the deque is empty, O(1)"""
        return self.size() == 0

    def capacity(self) -> int:
        """Get the capacity of the double-ended queue"""
        return self._capacity

    def _resize(self, new_capacity):
        """Resize the underlying array to the new capacity, O(n)"""
        new_deque = [None] * new_capacity
        curr_capacity = self.capacity()

        # Calculate the starting index
        start = (self._next_first + 1) % curr_capacity

        # Copy the elements to the new deque
        for i in range(self._size):
            new_deque[i] = self._deque[(start + i) % curr_capacity]

        self._deque = new_deque
        self._capacity = new_capacity
        self._next_first = new_capacity - 1
        self._next_last = self._size

    def add_first(self, val):
        """Add an item to the front of the deque, O(1) amortized"""
        if self.size() == self._capacity:
            self._resize(2 * self._capacity)
        self._deque[self._next_first] = val
        self._next_first = (self._next_first + self._capacity - 1) % self._capacity
        self._size += 1

    def add_last(self, val):
        """Add an item to the end of the deque, O(1) amortized"""
        size = self.size()
        capacity = self.capacity()
        if self.size() == capacity:
            self._resize(2 * capacity)
        self._deque[self._next_last] = val
        self._next_last = (self._next_last + 1) % self._capacity
        self._size += 1

    def remove_first(self):
        """Remove and return the item from the front of the deque, O(1) amortized"""
        if self.is_empty():
            raise IndexError("")
        if self._size < len(self._deque) // 4 + 1 and len(self._deque) > 20:
            self._resize(len(self._deque) // 2)
        self._next_first = (self._next_first + 1) % len(self._deque)
        item = self._deque[self._next_first]
        self._deque[self._next_first] = None
        self._size -= 1
        return item

    def remove_last(self):
        """Remove and return the item from the end of the deque, O(1) amortized"""
        if self.is_empty():
            return None
        if self._size < len(self._deque) // 4 + 1 and len(self._deque) > 20:
            self._resize(len(self._deque) // 2)
        self._next_last = (self._next_last - 1 + len(self._deque)) % len(self._deque)
        item = self._deque[self._next_last]
        self._deque[self._next_last] = None
        self._size -= 1
        return item

    def peek_first(self):
        front = (self._next_first + 1) % self.capacity()
        return self._deque[front]

    def peek_last(self):
        rear = (self._next_last - 1 + self.capacity()) % self.capacity()
        return self._deque[rear]

    def __repr__(self) -> str:
        """Return a string representation of the deque, O(n)"""
        return str(self)

    def __str__(self) -> str:
        """Return a string representation of the deque, O(n)"""
        res = [self._deque[(self._next_first + 1 + i) % len(self._deque)] for i in range(self._size)]
        return ' <- '.join(map(str, res))
