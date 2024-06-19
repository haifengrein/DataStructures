from Python.LinkedList.LinkedList import LinkedList
import pytest


@pytest.fixture
def sll():
    return LinkedList()


@pytest.fixture
def filled_sll():
    sll = LinkedList()
    values = [1, 2, 3, 4, 5]
    for val in values:
        sll.add_at_tail(val)
    return sll


class TestSinglyLinkedList:

    def test_initialize_empty_list(self, sll):
        assert sll.head is None

    def test_add_to_empty_list(self, sll):
        sll.add_at_tail(1)
        assert sll.head is not None
        assert sll.head._val == 1
        assert sll.head._next is None

    def test_add_at_head(self,filled_sll):
        filled_sll.add_at_head(10)
        assert str(filled_sll) == "10 - > 1 - > 2 - > 3 - > 4 - > 5 - > None"
        assert str(filled_sll.size) == "6"

    def test_add_at_index_head(self,filled_sll):
        filled_sll.add_at_index(0,10)
        assert str(filled_sll) == "10 - > 1 - > 2 - > 3 - > 4 - > 5 - > None"
        assert str(filled_sll.size) == "6"

    def test_add_at_index(self,filled_sll):
        filled_sll.add_at_index(1,10)
        assert str(filled_sll) == "1 - > 10 - > 2 - > 3 - > 4 - > 5 - > None"
        assert str(filled_sll.size) == "6"

    def test_add_at_index_tail(self,filled_sll):
        filled_sll.add_at_index(5,10)
        assert str(filled_sll) == "1 - > 2 - > 3 - > 4 - > 5 - > 10 - > None"
        assert str(filled_sll.size) == "6"


    def test_append_multiple_element(self, sll):
        values = [1, 2, 3, 4, 5]
        for val in values:
            sll.add_at_tail(val)
        current = sll.head
        for val in values:
            assert val == current._val
            current = current._next
        assert current is None

    def test_all_add_methods(self,sll):
        sll.add_at_head(1)
        sll.add_at_tail(3)
        sll.add_at_index(1,2)
        assert str(sll) == "1 - > 2 - > 3 - > None"



    def test_delete_at_index(self, filled_sll):
        filled_sll.delete_at_index(2)
        assert str(filled_sll) == "1 - > 2 - > 4 - > 5 - > None"

    def test_delete_at_head_index(self, filled_sll):
        filled_sll.delete_at_head()
        assert str(filled_sll) == "2 - > 3 - > 4 - > 5 - > None"

    def test_delete_at_tail_index(self, filled_sll):
        filled_sll.delete_at_tail()
        assert str(filled_sll) == "1 - > 2 - > 3 - > 4 - > None"


    def test_delete_single_element(self, filled_sll):
        filled_sll.delete_by_value(3)
        assert str(filled_sll) == "1 - > 2 - > 4 - > 5 - > None"

    def test_delete_mult_element(self, filled_sll):
        filled_sll.delete_by_value(3)
        filled_sll.delete_by_value(4)
        filled_sll.delete_by_value(5)
        assert str(filled_sll) == "1 - > 2 - > None"

    def test_delete_all_element(self, filled_sll):
        values = [1, 2, 3, 4, 5]
        assert str(filled_sll) == "1 - > 2 - > 3 - > 4 - > 5 - > None"
        for val in values:
            filled_sll.delete_by_value(val)
        assert str(filled_sll) == "None"

    def test_find_single_element(self, filled_sll):
        assert filled_sll.find(5) == 4

    def test_find_raises_exception(self, filled_sll):
        with pytest.raises(ValueError, match="Value 6 not found in the linked list."):
            filled_sll.find(6)

    def test_access_element(self, filled_sll):
        assert filled_sll.get(4) == 5

    def test_str_method(self, filled_sll):
        assert str(filled_sll) == "1 - > 2 - > 3 - > 4 - > 5 - > None"