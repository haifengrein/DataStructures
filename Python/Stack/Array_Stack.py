class ArrayStack:
    """Stack class based on array"""

    def __init__(self):
        """Constructor, O(1)"""
        self._stack: list[int] = []

    def size(self) -> int:
        """Get the length of the stack, O(1)"""
        return len(self._stack)

    def is_empty(self) -> bool:
        """Determine if the stack is empty, O(1)"""
        return self.size() == 0

    def push(self, val: int):
        """Push a value onto the stack, O(1) amortized"""
        return self._stack.append(val)

    def pop(self) -> int:
        """Pop the top value off the stack, O(1) amortized"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._stack.pop()

    def peek(self) -> int:
        """Access the top value of the stack, O(1)"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._stack[-1]

    def __repr__(self) -> str:
        """Return a string representation of the stack, O(n)"""
        return str(self)

    def __str__(self) -> str:
        """Return a string representation of the stack, O(n)"""
        return ' -> '.join(map(str, reversed(self._stack)))