# Stack

This module provides a basic implementation of stacks using both linked list and array structures in Python.

## Stack Implementations

### ArrayStack

The `ArrayStack` class implements a stack using a Python list. It provides the standard stack operations: push, pop, peek, size, and is_empty.

### LinkedListStack

The `LinkedListStack` class implements a stack using a linked list. It also provides the standard stack operations: push, pop, peek, size, and is_empty.

## Operations Complexity Comparison

| Operation   | ArrayStack     | LinkedListStack |
|-------------|-----------------|-----------------|
| `push`      | O(1) amortized  | O(1)            |
| `pop`       | O(1) amortized  | O(1)            |
| `peek`      | O(1)            | O(1)            |
| `size`      | O(1)            | O(1)            |
| `is_empty`  | O(1)            | O(1)            |

