"""
LinkedList Module
=================

This module provides a basic implementation of a singly linked list.

Classes:
--------
- ListNode
  - __init__(self, val=0, next=None)

- LinkedList
  - __init__(self)
  - add_at_head(self, val)
  - add_at_tail(self, val)
  - add_at_index(self, index: int, val)
  - delete_at_index(self, index: int)
  - delete_at_head(self, val)
  - delete_at_tail(self, val)
  - delete_by_value(self, val)
  - find(self, val)
  - get(self, index)
  - __len__(self)
  - __repr__(self)
  - __str__(self)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_at_head(self, val) -> None:
        """
        Add a new node with the given value at the head of the list.

        Parameters:
        val (any): The value to be appended to the list.
        """
        self.head = ListNode(val, self.head)
        self.size += 1

    def add_at_tail(self, val) -> None:
        """
        Append a new node with the given value to the end of the list.

        Parameters:
        val (any): The value to be appended to the list.
        """

        if not self.head:
            self.add_at_head(val)
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)
        self.size += 1

    def add_at_index(self, index: int, val) -> None:
        """
        Add a new node with the given value at the specified index.

        Parameters:
        index (int): The position at which to add the new node.
        val (any): The value to be added to the list.

        Raises:
        IndexError: If the index is out of bounds.
        """
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds.")
        if index == 0:
            self.add_at_head(val)
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next
        current.next = ListNode(val, current.next)
        self.size += 1

    def delete_at_index(self, index: int) -> None:
        """
        Delete the node at the specified index.

        Parameters:
        index (int): The position of the node to be deleted.

        Raises:
        IndexError: If the index is out of bounds.
        """
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds.")
        if index == 0:
            self.head = self.head.next
            return
        curr_node = self.head
        for _ in range(index - 1):
            curr_node = curr_node.next
        curr_node.next = curr_node.next.next
        self.size -= 1

    def delete_at_head(self) -> None:
        """
                Delete the node at the head.
        """
        return self.delete_at_index(0)

    def delete_at_tail(self) -> None:
        """
                        Delete the node at the tail.
        """
        return self.delete_at_index(self.size - 1)

    def delete_by_value(self, val) -> None:
        """
        Delete the first node with the given value from the list.

        Parameters:
        val (any): The value to be deleted from the list.

        Raises:
        IndexError: If the list is empty.
        ValueError: If the value is not found in the list.
        """
        if self.size == 0:
            raise IndexError("Can't delete from an empty linked list.")
        if self.head.val == val:
            self.head = self.head.next
            self.size -= 1
            return
        current = self.head
        while current.next and current.next.val != val:
            current = current.next

        if current.next is None:
            raise ValueError(f"Value {val} not found in the linked list.")
        current.next = current.next.next
        self.size -= 1

    def find(self, val) -> int:
        """
        Find the index of the first node with the given value.

        Parameters:
        val (any): The value to be found in the list.

        Returns:
        int: The index of the node with the given value.

        Raises:
        ValueError: If the value is not found in the list.
        """
        index = 0
        current = self.head
        while current:
            if current.val == val:
                return index
            current = current.next
            index += 1

        raise ValueError(f"Value {val} not found in the linked list.")

    def get(self, index) -> int:
        """
        Access the value of the node at the given index.

        Parameters:
        index (int): The index of the node to be accessed.

        Returns:
        any: The value of the node at the given index.

        Raises:
        IndexError: If the index is out of range.
        ValueError: If the list is empty.
        """
        if (index + 1) > self.size:
            raise IndexError("The index is bigger than the length of the linked list")
        current = self.head
        for _ in range(index):
            if not self.head:
                raise ValueError("Can't access from an empty linked list.")
            current = current.next
        return current.val

    def __len__(self):
        """Return the number of elements in the list."""
        return self.size

    def __repr__(self):
        """Return a string representation of the list."""
        result = []
        current = self.head
        while current:
            result.append(str(current.val))
            current = current.next
        result.append("None")
        return " - > ".join(result)

    def __str__(self):
        return self.__repr__()
