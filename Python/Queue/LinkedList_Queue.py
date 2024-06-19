class ListNode:
    """Node class for linked list"""

    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedListQueue:
    """Queue class based on linked list"""

    def __init__(self):
        """Constructor, O(1)"""
        self._front: ListNode | None = None
        self._rear: ListNode | None = None
        self._size: int = 0

    def size(self) -> int:
        """Get the length of the queue, O(1)"""
        return self._size

    def is_empty(self) -> bool:
        """Determine if the queue is empty, O(1)"""
        return self.size() == 0

    def enqueue(self, val: int):
        """Enqueue a value into rear of the queue, O(1)"""
        new_node = ListNode(val)
        if self.is_empty():
            self._front = new_node
            self._rear = new_node
        else:
            self._rear.next = new_node
            self._rear = new_node
        self._size += 1

    def dequeue(self) -> int:
        """Dequeue the front value from the queue, O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        res = self._front.val
        self._front = self._front.next
        self._size -= 1
        return res

    def peek(self) -> int:
        """Access the front value of the queue, O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._front.val

    def __repr__(self) -> str:
        """Return a string representation of the queue, O(n)"""
        return str(self)

    def __str__(self) -> str:
        """Return a string representation of the queue, O(n)"""
        arr = []
        curr_node = self._front
        while curr_node:
            arr.append(str(curr_node.val))
            curr_node = curr_node.next
        return " <- ".join(arr)
