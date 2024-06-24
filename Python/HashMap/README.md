# HashMap Module

This module provides two basic implementations of a HashMap in Python: 
- `HashMapChaining`: Uses separate chaining with array to handle collisions.
- `HashMapOpenAddressing`: Uses open addressing with linear probing to handle collisions.

## HashMap Chaining vs HashMap Open Addressing Table

| Operation           | HashMap Chaining | HashMap Open Addressing |
|---------------------|------------------|-------------------------|
| `put`               | O(1) on average  | O(1) on average         |
| `get`               | O(1) on average  | O(1) on average         |
| `remove`            | O(1) on average  | O(1) on average         |


## Design Rationale and Issues

**Issues**:

- **Clustering**: Linear probing can cause primary clustering, where consecutive filled slots increase the likelihood of further collisions, degrading performance.
- **Deletion Complications**: Direct deletion can disrupt the probing sequence, making it difficult to find elements that are placed after the deleted slot. 

**Lazy Deletion as a Solution**:

- **Marking Deletions**: Instead of removing elements, tombstones are used to mark deletions. This maintains the integrity of the probing sequence, ensuring that subsequent searches and insertions can still find the correct position of elements.
- **Optimization**: To address the accumulation of tombstones, the first encountered tombstone can be reused for new insertions. This helps to move elements closer to their ideal positions, thereby improving access times and reducing the impact of tombstone accumulation on performance.