class Pair:
    def __init__(self, key: int, val: str):
        self.key = key
        self.val = val

class HashMapOpenAddressing:

    def __init__(self):
        """
        Initializes the hash map with initial capacity and empty chains.
        Time Complexity: O(1)
        """
        self._size = 0
        self._capacity = 16
        self._load_factor = 0.75
        self._buckets: list[Pair | None] = [None] * self._capacity
        self._TOMBSTONE = Pair(-1, "-1")


    def hash_func(self, key: int) -> int:
        """
        Hash function to compute the index for a given key.
        """
        hash_val = hash(key)
        return self.flood_mod(hash_val, self._capacity)

    def flood_mod(self, hash_val: int, capacity: int) -> int:
        remainder = hash_val % capacity
        if remainder < 0:
            remainder += capacity
        return remainder

    def load_capacity(self) -> float:
        """
        Computes the load factor of the hash map.
        """
        return self._size / self._capacity

    def find_bucket(self, key: int) -> int:
        pos = self.hash_func(key)
        first_tombstone = -1
        while self._buckets[pos] is not None:
            if self._buckets[pos].key == key:
                if first_tombstone != -1:
                    self._buckets[first_tombstone] = self._buckets[pos]
                    self._buckets[pos] = self._TOMBSTONE
                    return first_tombstone
                return pos
            if first_tombstone == -1 and self._buckets[pos] is self._TOMBSTONE:
                first_tombstone = pos
            pos = (pos + 1) % self._capacity
        return pos if first_tombstone == -1 else first_tombstone


    def get(self, key: int) -> str:
        """
        Retrieves the value associated with the given key, if it exists.
        Time Complexity: O(1) on average
        """
        pos = self.find_bucket(key)
        if self._buckets[pos] not in [None, self._TOMBSTONE]:
            return self._buckets[pos].val
        raise KeyError(f"Key {key} not found in HashMap.")


    def put(self, key: int, val: str):
        """
        Inserts a key-value pair into the hash map.
        Time Complexity: O(1) on average
        """
        if self.load_capacity() > self._load_factor:
            self.resize()
        pos = self.find_bucket(key)
        if self._buckets[pos] not in [None, self._TOMBSTONE]:
            self._buckets[pos].val = val
            return
        self._buckets[pos] = Pair(key,val)
        self._size += 1

    def remove(self, key: int):
        """
        Removes the key-value pair associated with the given key, if it exists.
        Time Complexity: O(1) on average
        """
        pos = self.find_bucket(key)
        if self._buckets[pos] not in [None, self._TOMBSTONE]:
            self._buckets[pos] = self._TOMBSTONE
            self._size -= 1
        else:
            raise KeyError(f"Key {key} not found in HashMap.")


    def resize(self):
        """
        Doubles the capacity of the hash map and rehashes all existing key-value pairs.
        Time Complexity: O(n)
        """
        old_buckets = self._buckets
        self._capacity *= 2
        self._buckets = [None] * self._capacity
        self._size = 0
        for pair in old_buckets:
            if pair not in [None, self._TOMBSTONE]:
                self.put(pair.key, pair.val)

    def __str__(self):
        res = []
        for i, bucket in enumerate(self._buckets):
            if bucket is not None and bucket is not self._TOMBSTONE:
                res.append(f"Bucket {i}: {bucket.key} -> {bucket.val}")
        return "\n".join(res)

    def __repr__(self):
        return str(self)