import pytest
import random
from Python.Stack.Array_Stack import ArrayStack
from Python.Stack.LinkedList_Stack import LinkedListStack

@pytest.fixture
def array_stack():
    return ArrayStack()

@pytest.fixture
def linked_list_stack():
    return LinkedListStack()

@pytest.fixture
def built_in_stack():
    return []

class TestStack:
    @pytest.mark.parametrize("stack_type", [ArrayStack, LinkedListStack])
    def test_stack(self, stack_type):
        stack = stack_type()
        assert stack.is_empty() is True
        stack.push(10)
        assert stack.peek() == 10
        stack.push(20)
        assert stack.size() == 2
        assert stack.pop() == 20
        assert stack.peek() == 10
        stack.pop()
        assert stack.is_empty() is True

    def test_random_operations(self, array_stack, linked_list_stack, built_in_stack):
        for _ in range(100):
            value = random.randint(1, 100)
            array_stack.push(value)
            linked_list_stack.push(value)
            built_in_stack.append(value)

        operations = ['push', 'pop', 'peek']
        for _ in range(50000):
            op = random.choice(operations)
            if op == 'push':
                value = random.randint(1, 100)
                array_stack.push(value)
                linked_list_stack.push(value)
                built_in_stack.append(value)
            elif op == 'pop':
                if not built_in_stack:
                    continue
                expected = built_in_stack.pop()
                assert array_stack.pop() == expected
                assert linked_list_stack.pop() == expected
            elif op == 'peek':
                if not built_in_stack:
                    continue
                expected = built_in_stack[-1]
                assert array_stack.peek() == expected
                assert linked_list_stack.peek() == expected