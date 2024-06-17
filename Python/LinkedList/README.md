# LinkedList Module

This module provides a basic implementation of a Linked list & Double linked list in Python.

## Classes

### Linked List
#### ListNode
- `__init__(self, val=0, next=None)`

#### LinkedList Methods
- `__init__(self)`
- `add_at_head(self, val) -> None`
- `add_at_tail(self, val) -> None`
- `add_at_index(self, index: int, val) -> None`
- `delete_at_index(self, index: int) -> None`
- `delete_at_head(self, val) -> None`
- `delete_at_tail(self, val) -> None`
- `delete_by_value(self, val) -> None`
- `find(self, val) -> int`
- `get(self, index) -> int`
- `__len__(self)`
- `__repr__(self)`
- `__str__(self)`

### Double Linked List


## Singly vs Doubly Linked List Table

| Method            | Singly | Doubly |
|-------------------|-----------------|--------|
| `add_at_head`     | O(1)            | O(1)   |
| `add_at_tail`     | O(n)            | O(1)   |
| `add_at_index`    | O(n)            | O(1)   |
| `delete_at_index` | O(n)            | O(1)   |
| `delete_at_head`  | O(1)            | O(1)   |
| `delete_at_tail`  | O(1)            | O(1)   |
| `delete_by_value` | O(n)            | O(1)   |
| `find`            | O(n)            | O(1)   |
| `get`             | O(n)            | O(1)   |


