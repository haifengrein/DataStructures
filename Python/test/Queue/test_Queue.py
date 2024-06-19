import pytest
import random
from Python.Queue.Array_Queue import ArrayQueue
from Python.Queue.LinkedList_Queue import LinkedListQueue


@pytest.fixture
def array_queue():
    return ArrayQueue(10)  # 假设队列的最大容量为100

@pytest.fixture
def linked_list_queue():
    return LinkedListQueue()

class TestQueue:
    @pytest.mark.parametrize("queue_type", [ArrayQueue, LinkedListQueue])
    def test_queue(self, queue_type):
        queue = queue_type(100) if queue_type is ArrayQueue else queue_type()
        assert queue.is_empty() is True
        queue.enqueue(10)
        assert queue.peek() == 10
        queue.enqueue(20)
        assert queue.size() == 2
        assert queue.dequeue() == 10
        assert queue.peek() == 20
        queue.dequeue()
        assert queue.is_empty() is True

    def test_random_operations(self, array_queue, linked_list_queue):
        built_in_queue = []

        # 先 enqueue 100 个随机数
        for _ in range(100):
            value = random.randint(1, 100)
            array_queue.enqueue(value)
            linked_list_queue.enqueue(value)
            built_in_queue.append(value)

        operations = ['enqueue', 'dequeue', 'peek']
        for _ in range(10000):
            op = random.choice(operations)
            if op == 'enqueue':
                value = random.randint(1, 100)
                array_queue.enqueue(value)
                linked_list_queue.enqueue(value)
                built_in_queue.append(value)
            elif op == 'dequeue':
                if not built_in_queue:
                    continue
                expected = built_in_queue.pop(0)
                assert array_queue.dequeue() == expected
                assert linked_list_queue.dequeue() == expected
            elif op == 'peek':
                if not built_in_queue:
                    continue
                expected = built_in_queue[0]
                assert array_queue.peek() == expected
                assert linked_list_queue.peek() == expected

    def test_resize_operations(self, array_queue):
        initial_capacity = array_queue.capacity()

        for i in range(initial_capacity):
            array_queue.enqueue(i)

        array_queue.enqueue(initial_capacity)
        assert array_queue.capacity() > initial_capacity
        assert array_queue.size() == initial_capacity + 1

        for i in range(initial_capacity + 1):
            assert array_queue.dequeue() == i

        for i in range(initial_capacity * 2):
            array_queue.enqueue(i)

        for i in range(initial_capacity * 2):
            array_queue.dequeue()

        assert array_queue.capacity() < initial_capacity * 2
        assert array_queue.is_empty() is True

if __name__ == "__main__":
    pytest.main()