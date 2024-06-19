# Queue Module

This provides a basic implementation of queues using both linked list and array structures in Python.

## Operations Complexity Comparison

| Operation   | ArrayQueue      | LinkedListQueue |
|-------------|------------------|-----------------|
| `enqueue`   | O(1) amortized   | O(1)            |
| `dequeue`   | O(1)             | O(1)            |
| `peek`      | O(1)             | O(1)            |
| `size`      | O(1)             | O(1)            |
| `is_empty`  | O(1)             | O(1)            |

## Key Takeaways for ArrayQueue

The `ArrayQueue` class implements a queue using a Python list as a circular array. This allows the `dequeue` operation to be performed in O(1) time, whereas in a regular list implementation, it would take O(n) time due to the need to shift elements. The `ArrayQueue` provides the standard queue operations: enqueue, dequeue, peek, size, and is_empty.

To achieve O(1) time complexity for both `enqueue` and `dequeue` operations, we use a variable `front` to point to the index of the front element and maintain a variable `size` to record the length of the queue. The rear position can be calculated using the formula `rear = (front + size) % capacity`. This design ensures that the valid range of elements in the array is `[front, (front + size - 1) % capacity]`.

- Enqueue operation: Assign the input element to the `rear` index and increase `size` by 1.
- Dequeue operation: Increase `front` by 1 and decrease `size` by 1.


## Deque

## Operations Complexity Comparison

| Operation      | ArrayDeque (Circular Array) | LinkedListDeque (Doubly Linked List) |
|----------------|-----------------------------|--------------------------------------|
| `add_first`    | O(1) amortized              | O(1)                                 |
| `add_last`     | O(1) amortized              | O(1)                                 |
| `remove_first` | O(1) amortized              | O(1)                                 |
| `remove_last`  | O(1) amortized              | O(1)                                 |
| `peek_first`   | O(1)                        | O(1)                                 |
| `peek_last`    | O(1)                        | O(1)                                 |

### Key Takeaways for ArrayDeque

#### Challenges of Designing ArrayDeque with Resizing

1. **Space Management**: Avoid frequent and costly reallocations, ensuring add operations are O(1) amortized.

2. **Maintaining Element Order**: When resizing, correctly copy elements to preserve logical order, handling the wrap-around nature of the circular buffer.

3. **Balancing Additions and Removals**: Dynamically grow and shrink based on usage, choosing appropriate thresholds to avoid frequent resizing.

#### Solutions Implemented in ArrayDeque

1. **Tracking Indices with `next_first` and `next_last`**: Respectively point to the next add position at the front and end of the deque, avoiding element shifts and ensuring efficient additions and removals.

2. **Circular Array Design**: Utilize array space efficiently, with elements wrapping around array boundaries. `add_first` inserts from right to left, decrementing `next_first`. `add_last` inserts from left to right, incrementing `next_last`.

3. **Dynamic Resizing**: Double the capacity when full, halve the capacity when size is less than 1/4 of capacity and capacity exceeds a threshold, correctly copying the element order.ty when full, halve the capacity when size is less than 1/4 of capacity and capacity exceeds a threshold, correctly copying the element order.