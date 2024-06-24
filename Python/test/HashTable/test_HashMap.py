import pytest
import random
from Python.HashMap.HashMapChaining import HashMapChaining
from Python.HashMap.HashMapOpenAddressing import HashMapOpenAddressing

class TestHashMap:

    @pytest.fixture(params=[HashMapChaining, HashMapOpenAddressing])
    def hash_map(self, request):
        return request.param()

    def test_initialization(self, hash_map):
        assert hash_map._size == 0
        assert hash_map._capacity == 16
        assert hash_map._load_factor == 0.75
        assert len(hash_map._buckets) == 16
        for bucket in hash_map._buckets:
            assert bucket == [] if isinstance(hash_map, HashMapChaining) else bucket is None

    def test_put_and_get(self, hash_map):
        hash_map.put(1, "one")
        assert hash_map.get(1) == "one"
        hash_map.put(17, "seventeen")
        assert hash_map.get(17) == "seventeen"
        hash_map.put(1, "uno")
        assert hash_map.get(1) == "uno"

    def test_remove(self, hash_map):
        hash_map.put(1, "one")
        hash_map.remove(1)
        with pytest.raises(KeyError):
            hash_map.get(1)

    def test_resize(self, hash_map):
        for i in range(20):
            hash_map.put(i, str(i))
        assert hash_map._capacity > 16
        for i in range(20):
            assert hash_map.get(i) == str(i)

    def test_key_error(self, hash_map):
        with pytest.raises(KeyError):
            hash_map.get(100)

    def test_collision(self, hash_map):
        hash_map.put(1, "one")
        hash_map.put(17, "seventeen")  # Same bucket as key 1 in initial capacity
        assert hash_map.get(1) == "one"
        assert hash_map.get(17) == "seventeen"

    def test_random_operations(self, hash_map):
        reference = {}
        keys = list(range(100))
        random.shuffle(keys)

        for key in keys:
            val = str(key)
            hash_map.put(key, val)
            reference[key] = val

        for key in keys:
            assert hash_map.get(key) == reference[key]

        random.shuffle(keys)
        for key in keys[:50]:
            hash_map.remove(key)
            del reference[key]
            with pytest.raises(KeyError):
                hash_map.get(key)

        for key in keys[50:]:
            assert hash_map.get(key) == reference[key]

if __name__ == "__main__":
    pytest.main()