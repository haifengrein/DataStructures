import pytest
import random
from Python.Queue.Array_Deque import ArrayDeque
from Python.Queue.LinkedList_Deque import LinkedListDeque
from collections import deque
@pytest.fixture
def linked_list_deque():
    return LinkedListDeque()

class TestLinkedListDeque:
    def test_add_and_remove(self, linked_list_deque):
        deque = linked_list_deque
        assert deque.is_empty() is True
        deque.add_first(10)
        assert deque.peek_first() == 10
        deque.add_last(20)
        assert deque.size() == 2
        assert deque.remove_first() == 10
        assert deque.peek_first() == 20
        assert deque.remove_last() == 20
        assert deque.is_empty() is True

    def test_array_deque(self):
        deque = ArrayDeque()


        assert deque.is_empty() is True


        for i in range(101):
            deque.add_last(i)

        assert deque.size() == 101

        assert deque.peek_first() == 0
        assert deque.peek_last() == 100

        for i in range(81):
            assert deque.remove_first() == i

        assert deque.size() == 20

        assert deque.peek_first() == 81
        assert deque.peek_last() == 100

        for i in range(20):
            assert deque.remove_first() == 81 + i

        assert deque.is_empty() is True

    def test_array_deque_rand(self):
        array_deque = ArrayDeque()
        collections_deque = deque()

        assert array_deque.is_empty() is True
        assert len(collections_deque) == 0

        for i in range(500):
            operation = random.choice(['add_first', 'add_last'])
            value = random.randint(1, 1000)
            if operation == 'add_first':
                array_deque.add_first(value)
                collections_deque.appendleft(value)
            else:
                array_deque.add_last(value)
                collections_deque.append(value)

        operations = ['add_first', 'add_last', 'remove_first', 'remove_last']
        elements_added = []

        for _ in range(50000):
            operation = random.choice(operations)
            if operation == 'add_first':
                value = random.randint(1, 1000)
                array_deque.add_first(value)
                collections_deque.appendleft(value)
            elif operation == 'add_last':
                value = random.randint(1, 1000)
                array_deque.add_last(value)
                collections_deque.append(value)
            elif operation == 'remove_first' and not array_deque.is_empty():
                removed_array_deque = array_deque.remove_first()
                removed_collections_deque = collections_deque.popleft()
                assert removed_array_deque == removed_collections_deque
            elif operation == 'remove_last' and not array_deque.is_empty():
                removed_array_deque = array_deque.remove_last()
                removed_collections_deque = collections_deque.pop()
                assert removed_array_deque == removed_collections_deque

            if array_deque._size == len(array_deque._deque):
                print(f"Resized up at size {array_deque._size}")
            if array_deque._size < len(array_deque._deque) // 4 and len(array_deque._deque) > 10:
                print(f"Resized down at size {array_deque._size}")


        assert array_deque.size() == len(collections_deque)
        if not array_deque.is_empty():
            assert array_deque.peek_first() == collections_deque[0]
            assert array_deque.peek_last() == collections_deque[-1]
        else:
            assert array_deque.size() == 0


        while not array_deque.is_empty():
            array_deque.remove_first()
            collections_deque.popleft()


        assert array_deque.is_empty() is True
        assert array_deque.size() == 0
        assert len(collections_deque) == 0

        print("All tests passed.")

    def test_random_operations(self, linked_list_deque):
        ll_deque = linked_list_deque
        built_in_deque = deque()

        # 先 add 100 个随机数
        for _ in range(100):
            value = random.randint(1, 100)
            ll_deque.add_last(value)
            built_in_deque.append(value)

        operations = ['add_first', 'add_last', 'remove_first', 'remove_last', 'peek_first', 'peek_last']
        for _ in range(10000):
            op = random.choice(operations)
            if op == 'add_first':
                value = random.randint(1, 100)
                ll_deque.add_first(value)
                built_in_deque.appendleft(value)
            elif op == 'add_last':
                value = random.randint(1, 100)
                ll_deque.add_last(value)
                built_in_deque.append(value)
            elif op == 'remove_first':
                if not built_in_deque:
                    continue
                expected = built_in_deque.popleft()
                assert ll_deque.remove_first() == expected
            elif op == 'remove_last':
                if not built_in_deque:
                    continue
                expected = built_in_deque.pop()
                assert ll_deque.remove_last() == expected
            elif op == 'peek_first':
                if not built_in_deque:
                    continue
                expected = built_in_deque[0]
                assert ll_deque.peek_first() == expected
            elif op == 'peek_last':
                if not built_in_deque:
                    continue
                expected = built_in_deque[-1]
                assert ll_deque.peek_last() == expected