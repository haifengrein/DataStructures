"""
LinkedList Module
=================

This module provides a basic implementation of a doubly linked list.

In this implementation, use a "two-sentinel" design pattern.

Core Summary of Doubly Linked List Implementation:

===================================================

	1.	Addition Operation:
	•	Traverse to the node immediately before or after the target position.
	•	The new node should point to the nodes before and after the intended position.
	•	Update the pointers of the adjacent nodes to correctly point to the new node.
	2.	Deletion Operation:
	•	Traverse to the node that needs to be deleted.
	•	Update the pointers of the node’s previous and next nodes to bypass the node to be deleted.
	•	When using the binary traversal method, ensure the traversal position is accurate.

Classes:
--------
- Node
  - __init__(self, value=None, prev=None, next=None)

- DoublyLinkedList
  - __init__(self)
  - add_at_head(self, val)
  - add_at_tail(self, val)
  - add_at_index(self, index: int, val)
  - delete_at_index(self, index: int)
  - delete_at_head(self)
  - delete_at_tail(self)
  - delete_by_value(self, val)
  - get(self, index)
  - get_size(self)
  - is_empty(self)
  - clear(self)
"""


class ListNode:

    def __init__(self, value=None, prev=None, next=None):
        self._val: int = value
        self._prev: ListNode = prev
        self._next: ListNode = next


class DoublyLinkedList:

    def __init__(self):
        self._head = ListNode()
        self._tail = ListNode()
        self._size = 0
        self._head._next = self._tail
        self._tail._prev = self._head

    def __len__(self):
        return self._size

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        result = []
        current = self._head._next
        result.append("None")
        while current is not self._tail:
            result.append(str(current._val))
            current = current._next
        result.append("None")
        return " <-> ".join(result)

    def add_at_head(self, val) -> None:
        """Add a value at the head of the list. O(1)"""
        new_node = ListNode(val, self._head, self._head._next)
        self._head._next._prev = new_node
        self._head._next = new_node
        self._size += 1

    def add_at_tail(self, val) -> None:
        """Add a value at the tail of the list. O(1)"""
        new_node = ListNode(val, self._tail._prev, self._tail)

        # Update 2 pointers to insert the new node
        self._tail._prev._next = new_node
        self._tail._prev = new_node
        self._size += 1

    def add_at_index(self, index: int, val) -> None:
        """Add a value at the specified index in the list. O(n)"""
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.add_at_head(val)
            return
        if index == self._size:
            self.add_at_tail(val)
            return
        if index < self._size // 2:
            curr_node = self._head._next
            for _ in range(index - 1):
                curr_node = curr_node._next
            new_node = ListNode(val, curr_node, curr_node._next)
            curr_node._next._prev = new_node
            curr_node._next = new_node
        else:
            curr_node = self._tail._prev
            for _ in range(self._size - index - 1):
                curr_node = curr_node._prev
            new_node = ListNode(val, curr_node._prev, curr_node)
            curr_node._prev._next = new_node
            curr_node._prev = new_node
        self._size += 1

    def delete_at_head(self) -> None:
        """Delete the value at the head of the list. O(1)"""
        if self._size == 0:
            raise ValueError("Can't delete from an empty linked list.")
        self._head._next = self._head._next._next
        self._head._next._prev = self._head
        self._size -= 1

    def delete_at_tail(self) -> None:
        """Delete the value at the tail of the list. O(1)"""
        if self._size == 0:
            raise ValueError("Can't delete from an empty linked list.")
        self._tail._prev = self._tail._prev._prev
        self._tail._prev._next = self._tail
        self._size -= 1

    def delete_at_index(self, index: int) -> None:
        """Delete the value at the specified index in the list. O(n)"""
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.delete_at_head()
            return
        if index == self._size - 1:
            self.delete_at_tail()
            return
        if index < self._size // 2:
            curr_node = self._head._next
            for _ in range(index):
                curr_node = curr_node._next
        else:
            curr_node = self._tail._prev
            for _ in range(self._size - index - 1):
                curr_node = curr_node._prev
        curr_node._prev._next = curr_node._next
        curr_node._next._prev = curr_node._prev
        self._size -= 1

    def delete_by_value(self, val) -> None:
        """Delete the first occurrence of the value in the list. O(n)"""
        if self._size == 0:
            raise ValueError("Can't delete from an empty linked list.")

        if self._head._next._val == val or self._tail._prev._val == val:
            if self._head._next._val == val:
                self.delete_at_head()
            else:
                self.delete_at_tail()
            return

        head_node = self._head._next
        tail_node = self._tail._prev
        while head_node._val != val and tail_node._val != val and head_node != tail_node:
            head_node = head_node._next
            tail_node = tail_node._prev

        if head_node == tail_node and head_node._val != val:
            raise ValueError(f"Value {val} not found in the linked list.")

        if head_node._val == val:
            head_node._prev._next = head_node._next
            head_node._next._prev = head_node._prev
        else:
            tail_node._prev._next = tail_node._next
            tail_node._next._prev = tail_node._prev

        self._size -= 1

    def get(self, index: int):
        """Get the value at the specified index in the list. O(n)"""
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")

        if index < self._size // 2:
            curr_node = self._head._next
            for _ in range(index):
                curr_node = curr_node._next
        else:
            curr_node = self._tail._prev
            for _ in range(self._size - index - 1):
                curr_node = curr_node._prev
        return curr_node._val

    def get_size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def clear(self) -> None:
        """Clear the list. O(1)"""
        self._head._next = self._tail
        self._tail._prev = self._head
        self._size = 0
