class Pair:
     def __init__(self, key: int, val: str):
        self.key = key
        self.val = val
class HashMapChaining:

    def __init__(self):
        """
        Initializes the hash map with initial capacity and empty chains.
        Time Complexity: O(1)
        """
        self._size = 0
        self._capacity = 16
        self._load_factor = 0.75
        self._buckets = [[] for _ in range(self._capacity)]


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

    def get(self, key: int) -> str | None:
        """
        Retrieves the value associated with the given key, if it exists.
        Time Complexity: O(1) on average
        """
        hash_val = self.hash_func(key)
        target_bucket = self._buckets[hash_val]
        for pair in target_bucket:
            if pair.key == key:
                return pair.val
        raise KeyError(f"Key {key} not found in HashMap.")
    def put(self, key: int, val: str):
        """
        Inserts a key-value pair into the hash map.
        Time Complexity: O(1) on average
        """
        if self.load_capacity() > self._load_factor:
            self.resize()

        hash_val = self.hash_func(key)
        target_bucket = self._buckets[hash_val]
        for pair in target_bucket:
            if pair.key == key:
                pair.val = val
                return
        target_bucket.append(Pair(key,val))
        self._size += 1

    def remove(self, key: int):
        """
        Removes the key-value pair associated with the given key, if it exists.
        Time Complexity: O(1) on average
        """
        hash_val = self.hash_func(key)
        target_bucket = self._buckets[hash_val]
        for pair in target_bucket:
            if pair.key == key:
                target_bucket.remove(pair)
                self._size -= 1
                return
        raise KeyError(f"Key {key} not found in HashMap.")

    def resize(self):
        """
        Doubles the capacity of the hash map and rehashes all existing key-value pairs.
        Time Complexity: O(n)
        """
        old_buckets = self._buckets
        self._capacity *= 2
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0
        for bucket in old_buckets:
            for pair in bucket:
                self.put(pair.key, pair.val)
    def __str__(self):
        res = []
        for i, bucket in enumerate(self._buckets):
            if bucket:
                bucket_str = ", ".join([f"{pair.key} -> {pair.val}" for pair in bucket])
                res.append(f"Bucket {i}: {bucket_str}")
        return "\n".join(res)

    def __repr__(self):
        return str(self)