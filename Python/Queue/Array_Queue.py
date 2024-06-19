class ArrayQueue:
    """Queue class based on array"""

    def __init__(self, max_capacity: int):
        """Constructor, O(1)"""
        self._queue: list[int] = [0] * max_capacity
        self._front: int = 0
        self._size: int = 0

    def capacity(self) -> int:
        return len(self._queue)

    def size(self) -> int:
        """Get the length of the queue, O(1)"""
        return self._size

    def is_empty(self) -> bool:
        """Determine if the queue is empty, O(1)"""
        return self.size() == 0

    def enqueue(self, val: int):
        """Enqueue a value into the queue, O(1) amortized"""
        if self._size == self.capacity():
            self.resize(2 * self.capacity())
        rear: int = (self._front + self._size) % self.capacity()
        self._queue[rear] = val
        self._size += 1

    def dequeue(self) -> int:
        """Dequeue the front value from the queue, O(1)"""
        if (self._size / self.capacity()) < 0.5:
            self.resize(int(0.6 * self.capacity()))
        num: int = self.peek()
        self._front = (self._front + 1) % self.capacity()
        self._size -= 1
        return num

    def peek(self) -> int:
        """Access the front value of the queue, O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._queue[self._front]

    def resize(self, new_capacity:int):
        old_queue = self._queue
        self._queue = [0] * new_capacity
        for i in range(self._size):
            self._queue[i] = old_queue[(self._front + i) % len(old_queue)]
        self._front = 0

    def __repr__(self) -> str:
        """Return a string representation of the queue, O(n)"""
        return str(self)

    def __str__(self) -> str:
        """Return a string representation of the queue, O(n)"""
        res = [0] * self.size()
        j: int = self._front
        for i in range(self.size()):
            res[i] = self._queue[j % self.capacity()]
            j += 1
        return ' <- '.join(map(str, res))
