class ListNode:
    """Node class for LinkedList"""
    def __init__(self, val: int = None, prev: 'ListNode' = None, next: 'ListNode' = None):
        self.val = val
        self.next = next
        self.prev = prev

class LinkedListDeque:
    """Deque class based on doubly linked list with circular sentinel topology"""

    def __init__(self):
        """Constructor, O(1)"""
        self._sentinel: ListNode = ListNode()
        self._sentinel.prev = self._sentinel
        self._sentinel.next = self._sentinel
        self._size: int = 0

    def size(self) -> int:
        """Get the length of the deque, O(1)"""
        return self._size

    def is_empty(self) -> bool:
        """Determine if the deque is empty, O(1)"""
        return self._size == 0

    def add_first(self, val: int):
        """Add a value to the front of the deque, O(1)"""
        new_node = ListNode(val,self._sentinel,self._sentinel.next)
        self._sentinel.next.prev = new_node
        self._sentinel.next = new_node
        self._size += 1

    def add_last(self, val: int):
        """Add a value to the end of the deque, O(1)"""
        new_node = ListNode(val, self._sentinel.prev, self._sentinel)
        self._sentinel.prev.next = new_node
        self._sentinel.prev = new_node
        self._size += 1

    def remove_first(self) -> int:
        """Remove and return the value from the front of the deque, O(1)"""
        res = self.peek_first()
        self._sentinel.next = self._sentinel.next.next
        self._sentinel.next.prev = self._sentinel
        self._size -= 1
        return res

    def remove_last(self) -> int:
        """Remove and return the value from the end of the deque, O(1)"""
        res = self.peek_last()
        self._sentinel.prev = self._sentinel.prev.prev
        self._sentinel.prev.next = self._sentinel
        self._size -= 1
        return res

    def peek_first(self) -> int:
        """Access the value at the front of the deque, O(1)"""
        if self.is_empty():
            raise IndexError("The Deque is empty.")
        res = self._sentinel.next.val
        return res

    def peek_last(self) -> int:
        """Access the value at the end of the deque, O(1)"""
        if self.is_empty():
            raise IndexError("The Deque is empty.")
        res = self._sentinel.prev.val
        return res

    def __repr__(self) -> str:
        """Return a string representation of the deque, O(n)"""
        return self.__str__()

    def __str__(self) -> str:
        """Return a string representation of the deque, O(n)"""
        curr_node = self._sentinel.next
        res = []
        for _ in range(self.size()):
            res.append(str(curr_node.val))
            curr_node = curr_node.next
        return " <-> ".join(res)