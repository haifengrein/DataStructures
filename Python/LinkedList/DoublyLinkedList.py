"""
LinkedList Module
=================

This module provides a basic implementation of a doubly linked list.

In this implementation, use a "two-sentinel" design pattern. The two sentinels are special nodes that do not store
any actual data; Instead, they serve as placeholders at the beginning (head) and end (tail) of the list. This design
simplifies the implementation by eliminating the need for special-case code to handle insertions and deletions at the
boundaries of the list.

The key benefits of using the two-sentinel pattern include: 1. Simplified code for insertion and deletion: With
sentinels, the head and tail nodes are always present, so there is no need to check for null references or handle
empty list conditions specially. 2. Improved readability and maintainability: The code is cleaner and easier to
understand, as it avoids edge cases that would otherwise complicate the logic.

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
        self.val = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def __len__(self):
        return self.size

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        result = []
        current = self.head.next
        result.append("None")
        while current is not self.tail:
            result.append(str(current.val))
            current = current.next
        result.append("None")
        return " <-> ".join(result)

    def add_at_head(self, val) -> None:
        """Add a value at the head of the list. O(1)"""
        new_node = ListNode(val, self.head, self.head.next)
        self.head.next.prev = new_node
        self.head.next = new_node
        self.size += 1

    def add_at_tail(self, val) -> None:
        """Add a value at the tail of the list. O(1)"""
        new_node = ListNode(val, self.tail.prev, self.tail)

        # Update 2 pointers to insert the new node
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.size += 1

    def add_at_index(self, index: int, val) -> None:
        """Add a value at the specified index in the list. O(n)"""
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.add_at_head(val)
            return
        if index == self.size:
            self.add_at_tail(val)
            return
        if index < self.size // 2:
            curr_node = self.head.next
            for _ in range(index - 1):
                curr_node = curr_node.next
            new_node = ListNode(val, curr_node, curr_node.next)
            curr_node.next.prev = new_node
            curr_node.next = new_node
        else:
            curr_node = self.tail.prev
            for _ in range(self.size - index - 1):
                curr_node = curr_node.prev
            new_node = ListNode(val, curr_node.prev, curr_node)
            curr_node.prev.next = new_node
            curr_node.prev = new_node
        self.size += 1

    def delete_at_head(self) -> None:
        """Delete the value at the head of the list. O(1)"""
        if self.size == 0:
            raise ValueError("Can't delete from an empty linked list.")
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.size -= 1

    def delete_at_tail(self) -> None:
        """Delete the value at the tail of the list. O(1)"""
        if self.size == 0:
            raise ValueError("Can't delete from an empty linked list.")
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        self.size -= 1

    def delete_at_index(self, index: int) -> None:
        """Delete the value at the specified index in the list. O(n)"""
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.delete_at_head()
            return
        if index == self.size - 1:
            self.delete_at_tail()
            return
        if index < self.size // 2:
            curr_node = self.head.next
            for _ in range(index):
                curr_node = curr_node.next
        else:
            curr_node = self.tail.prev
            for _ in range(self.size - index - 1):
                curr_node = curr_node.prev
        curr_node.prev.next = curr_node.next
        curr_node.next.prev = curr_node.prev
        self.size -= 1

    def delete_by_value(self, val) -> None:
        """Delete the first occurrence of the value in the list. O(n)"""
        if self.size == 0:
            raise ValueError("Can't delete from an empty linked list.")

        if self.head.next.val == val or self.tail.prev.val == val:
            if self.head.next.val == val:
                self.delete_at_head()
            else:
                self.delete_at_tail()
            return

        head_node = self.head.next
        tail_node = self.tail.prev
        while head_node.val != val and tail_node.val != val and head_node != tail_node:
            head_node = head_node.next
            tail_node = tail_node.prev

        if head_node == tail_node and head_node.val != val:
            raise ValueError(f"Value {val} not found in the linked list.")

        if head_node.val == val:
            head_node.prev.next = head_node.next
            head_node.next.prev = head_node.prev
        else:
            tail_node.prev.next = tail_node.next
            tail_node.next.prev = tail_node.prev

        self.size -= 1

    def get(self, index: int):
        """Get the value at the specified index in the list. O(n)"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        if index < self.size // 2:
            curr_node = self.head.next
            for _ in range(index):
                curr_node = curr_node.next
        else:
            curr_node = self.tail.prev
            for _ in range(self.size - index - 1):
                curr_node = curr_node.prev
        return curr_node.val

    def get_size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def clear(self) -> None:
        """Clear the list. O(1)"""
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
