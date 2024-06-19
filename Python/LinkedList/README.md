# LinkedList Module

This module provides a basic implementation of a Linked list & Double linked list in Python.


## Singly vs Doubly Linked List Table

| Operation           | Doubly Linked List | Singly Linked List|
|---------------------|-------------------------------------|-------------------------------------|
| `add_at_head`       | O(1)                                | O(1)                                |
| `add_at_tail`       | O(1)                                | O(n)                                |
| `add_at_index`      | O(n)                                | O(n)                                |
| `delete_at_head`    | O(1)                                | O(1)                                |
| `delete_at_tail`    | O(1)                                | O(n)                                |
| `delete_at_index`   | O(n)                                | O(n)                                |
| `delete_by_value`   | O(n)                                | O(n)                                |
| `get`               | O(n)                                | O(n)                                |
| `get_size`          | O(1)                                | O(1)                                |
| `is_empty`          | O(1)                                | O(1)                                |
| `clear`             | O(1)                                | O(1)                                |

## Key Takeaways for Doubly Linked List

### Addition Operation:
- Traverse to the node immediately before or after the target position.
- The new node should point to the nodes before and after the intended position.
- Update the pointers of the adjacent nodes to correctly point to the new node.

### Deletion Operation:
- Traverse to the node that needs to be deleted.
- Update the pointers of the node’s previous and next nodes to bypass the node to be deleted.
- When using the binary traversal method, ensure the traversal position is accurate.

