from Python.LinkedList.DoublyLinkedList import DoublyLinkedList
import pytest
import random
import timeit

@pytest.fixture
def dll():
    return DoublyLinkedList()

@pytest.fixture
def filled_dll():
    dll = DoublyLinkedList()
    for val in range(1, 10):
        dll.add_at_tail(val)
    return dll

class TestDoublyLinkedList:
    def test_initialize_empty_list(self, dll):
        assert dll.head is not None, "Head node should be initialized"
        assert dll.tail is not None, "Tail node should be initialized"
        assert dll.head.next is dll.tail, "Head's next should be tail"
        assert dll.tail.prev is dll.head, "Tail's prev should be head"
        assert dll.size == 0, "Size of the list should be initialized to 0"

    def test_add_to_head_empty_list(self, dll):
        dll.add_at_head(1)
        assert dll.head.next.val == 1
        assert dll.head.next.next is dll.tail
        assert dll.tail.prev.val == 1
        assert dll.size == 1

    def test_add_to_tail_empty_list(self, dll):
        dll.add_at_tail(1)
        assert dll.tail.prev.val == 1
        assert dll.tail.prev.prev is dll.head
        assert dll.head.next.val == 1
        assert dll.size == 1

    def test_add_method(self, dll):
        dll.add_at_head(2)
        dll.add_at_head(1)
        dll.add_at_tail(4)
        dll.add_at_tail(5)
        dll.add_at_tail(6)
        dll.add_at_index(2, 3)

        assert str(dll) == "None <-> 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <-> None"
        assert dll.size == 6

    def test_remove_method(self, filled_dll):
        filled_dll.delete_at_head()
        assert str(filled_dll) == "None <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <-> 7 <-> 8 <-> 9 <-> None"
        assert filled_dll.size == 8

        filled_dll.delete_at_tail()
        assert str(filled_dll) == "None <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <-> 7 <-> 8 <-> None"
        assert filled_dll.size == 7

        filled_dll.delete_at_head()
        filled_dll.delete_at_tail()
        assert str(filled_dll) == "None <-> 3 <-> 4 <-> 5 <-> 6 <-> 7 <-> None"
        assert filled_dll.size == 5

        filled_dll.delete_by_value(4)
        assert str(filled_dll) == "None <-> 3 <-> 5 <-> 6 <-> 7 <-> None"
        assert filled_dll.size == 4

        filled_dll.delete_by_value(3)
        assert str(filled_dll) == "None <-> 5 <-> 6 <-> 7 <-> None"
        assert filled_dll.size == 3

        with pytest.raises(ValueError):
            filled_dll.delete_by_value(100)

    def test_delete_at_index_method(self, filled_dll):
        filled_dll.delete_at_index(0)
        assert str(filled_dll) == "None <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <-> 7 <-> 8 <-> 9 <-> None"
        assert filled_dll.size == 8

        filled_dll.delete_at_index(7)
        assert str(filled_dll) == "None <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <-> 7 <-> 8 <-> None"
        assert filled_dll.size == 7

        filled_dll.delete_at_index(3)
        assert str(filled_dll) == "None <-> 2 <-> 3 <-> 4 <-> 6 <-> 7 <-> 8 <-> None"
        assert filled_dll.size == 6

        with pytest.raises(IndexError):
            filled_dll.delete_at_index(100)

    def test_get_method(self, filled_dll):
        assert filled_dll.get(0) == 1
        assert filled_dll.get(1) == 2
        assert str(filled_dll) == "None <-> 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <-> 7 <-> 8 <-> 9 <-> None"
        assert filled_dll.get(2) == 3
        assert filled_dll.get(3) == 4
        assert filled_dll.get(4) == 5
        assert filled_dll.get(5) == 6
        assert filled_dll.get(6) == 7
        assert filled_dll.get(7) == 8
        assert filled_dll.get(8) == 9

        with pytest.raises(IndexError):
            filled_dll.get(100)

    def test_clear_method(self, filled_dll):
        filled_dll.clear()
        assert filled_dll.size == 0
        assert filled_dll.head.next is filled_dll.tail
        assert filled_dll.tail.prev is filled_dll.head
        assert str(filled_dll) == "None <-> None"

    def test_adding_operations(self):

        my_list = DoublyLinkedList()
        ref_list = []

        N = 2500

        for _ in range(N):
            operation_number = random.randint(0, 2)

            if operation_number == 0:
                rand_val = random.randint(0, 100)
                my_list.add_at_tail(rand_val)
                ref_list.append(rand_val)

            elif operation_number == 1:
                rand_val = random.randint(0, 100)
                my_list.add_at_head(rand_val)
                ref_list.insert(0, rand_val)

            elif operation_number == 2:
                rand_val = random.randint(0, 100)
                index = random.randint(0, len(ref_list))
                my_list.add_at_index(index, rand_val)
                ref_list.insert(index, rand_val)

            assert my_list.get_size() == len(ref_list)

            for i in range(len(ref_list)):
                assert my_list.get(i) == ref_list[i]

    def test_deleting_operations(self):

        my_list = DoublyLinkedList()
        ref_list = []


        for _ in range(2500):
            rand_val = random.randint(0, 100)
            my_list.add_at_tail(rand_val)
            ref_list.append(rand_val)


        N = 2500

        for _ in range(N):
            if len(ref_list) == 0:
                continue

            operation_number = random.randint(0, 2)

            if operation_number == 0 and len(ref_list) > 0:
                my_list.delete_at_tail()
                ref_list.pop()

            elif operation_number == 1 and len(ref_list) > 0:
                my_list.delete_at_head()
                ref_list.pop(0)

            elif operation_number == 2 and len(ref_list) > 0:
                index = random.randint(0, len(ref_list) - 1)
                my_list.delete_at_index(index)
                ref_list.pop(index)

            assert my_list.get_size() == len(ref_list)


            for i in range(len(ref_list)):
                assert my_list.get(i) == ref_list[i]

    def test_randomized_operations(self):
        my_list = DoublyLinkedList()
        ref_list = []

        N = 500000

        for _ in range(N):
            operation_number = random.randint(0, 7)

            if operation_number == 0:
                rand_val = random.randint(0, 100)
                my_list.add_at_tail(rand_val)
                ref_list.append(rand_val)

            elif operation_number == 1:
                assert my_list.get_size() == len(ref_list)

            elif operation_number == 2 and len(ref_list) > 0:
                assert my_list.get(my_list.get_size() - 1) == ref_list[-1]

            elif operation_number == 3 and len(ref_list) > 0:
                my_list.delete_at_tail()
                ref_list.pop()

            elif operation_number == 4:
                rand_val = random.randint(0, 100)
                my_list.add_at_head(rand_val)
                ref_list.insert(0, rand_val)

            elif operation_number == 5 and len(ref_list) > 0:
                my_list.delete_at_head()
                ref_list.pop(0)

            elif operation_number == 6:
                rand_val = random.randint(0, 100)
                index = random.randint(0, len(ref_list))
                my_list.add_at_index(index, rand_val)
                ref_list.insert(index, rand_val)

            elif operation_number == 7 and len(ref_list) > 0:
                index = random.randint(0, len(ref_list) - 1)
                my_list.delete_at_index(index)
                ref_list.pop(index)

    def test_time_complexity_add_at_tail(self):
        def wrapper_dll_add(dll, val):
            dll.add_at_tail(val)

        def wrapper_list_add(lst, val):
            lst.append(val)

        dll_times = []
        list_times = []

        for i in range(1000, 10001, 1000):
            dll = DoublyLinkedList()
            lst = []

            dll_time = timeit.timeit(lambda: wrapper_dll_add(dll, 1), number=i)
            list_time = timeit.timeit(lambda: wrapper_list_add(lst, 1), number=i)

            dll_times.append(dll_time)
            list_times.append(list_time)

        print("Add at tail times for DoublyLinkedList:", dll_times)
        print("Add at tail times for built-in list:", list_times)

    def test_time_complexity_delete_at_tail(self):
        def wrapper_dll_delete(dll):
            dll.delete_at_tail()

        def wrapper_list_delete(lst):
            lst.pop()

        dll_times = []
        list_times = []

        for i in range(1000, 10001, 1000):
            dll = DoublyLinkedList()
            lst = []
            for _ in range(i):
                dll.add_at_tail(1)
                lst.append(1)

            dll_time = timeit.timeit(lambda: wrapper_dll_delete(dll), number=i)
            list_time = timeit.timeit(lambda: wrapper_list_delete(lst), number=i)

            dll_times.append(dll_time)
            list_times.append(list_time)

        print("Delete at tail times for DoublyLinkedList:", dll_times)
        print("Delete at tail times for built-in list:", list_times)

if __name__ == "__main__":
    pytest.main()
