
class ListNode():

    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class LinkedListStack:
    """Stack class based on linked list"""

    def __init__(self):
        """Constructor, O(1)"""
        self._top: ListNode | None = None
        self._size: int = 0

    def size(self) -> int:
        """Get the length of the stack, O(1)"""
        return self._size

    def is_empty(self) -> bool:
        """Determine if the stack is empty, O(1)"""
        return self._size == 0

    def push(self, val: int):
        """Push a value onto the stack, O(1)"""
        self._top = ListNode(val,self._top)
        self._size += 1

    def pop(self) -> int:
        """Pop the top value off the stack, O(1)"""
        res = self.peek()
        self._top = self._top.next
        self._size -= 1
        return res

    def peek(self) -> int:
        """Access the top value of the stack, O(1)"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._top.val

    def __repr__(self) -> str:
        """Return a string representation of the stack, O(n)"""
        arr = []
        curr_node = self._top
        while curr_node:
            arr.append(curr_node.val)
            curr_node = curr_node.next
        arr.reverse()
        return ' -> '.join(map(str, arr))

    def __str__(self) -> str:
        """Return a string representation of the stack, O(n)"""
        return self.__repr__()