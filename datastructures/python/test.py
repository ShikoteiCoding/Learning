import unittest

from arrays import (Stack, Queue, LinkedList)

class TestStack(unittest.TestCase):
    """ Test the stack expected behavior. """

    def setUp(self):
        self.stack = Stack()

    def test_empty(self):
        self.assertEqual(len(self.stack), 0)

    def test_add_elements(self):
        for i in range(3): self.stack.add(i)

        self.assertEqual(len(self.stack), 3)

    def test_remove_elements(self):
        for i in range(3): self.stack.add(i)
        
        li = self.stack.remove()

        self.assertEqual(len(self.stack), 2)
        self.assertEqual(li, 2) # Last element was 2
        self.assertEqual(self.stack, [0, 1])

    def test_limits(self):
        self.assertRaises(IndexError, self.stack.remove)

class TestQueue(unittest.TestCase):
    """ Test the queue expected behavior. """

    def setUp(self):
        self.queue = Queue()
    
    def test_empty(self):
        self.assertEqual(len(self.queue), 0)

    def test_add_elements(self):
        for i in range(3): self.queue.add(i)

        self.assertEqual(len(self.queue), 3)

    def test_remove_elements(self):
        for i in range(3): self.queue.add(i)

        fi = self.queue.remove()

        self.assertEqual(len(self.queue), 2)
        self.assertEqual(fi, 0) # First element
        self.assertEqual(self.queue, [1, 2])

    def test_limits(self):
        self.assertRaises(IndexError, self.queue.remove)

class TestLinkedList(unittest.TestCase):
    """ Test of linked list expected behavior. """

    def setUp(self):
        self.llist = LinkedList()

    def test_empty(self):
        self.assertEqual(len(self.llist), 0)

    def test_add_element(self):
        for i in range(3): self.llist.add(i)

        self.assertEqual(len(self.llist), 3)

    def test_remove_element(self):
        for i in range(3): self.llist.add(i)

        li = self.llist.remove() # remove the last element

        self.assertEqual(len(self.llist), 2)
        self.assertEqual(li, 2)
        self.assertEqual(self.llist, [0, 1])

    def test_find_first_element_index_with_value_offset(self):
        """ Index position is not value. """
        for i in range(10): self.llist.add(i - 1)
        values = [0, 2, 5]
        indexes = [1, 3, 6]
        found_indexes = [self.llist.find_first(value) for value in values]
        self.assertEqual(found_indexes, indexes)

    def test_remove_element_by_index(self):
        for i in range(10): self.llist.add(i)
        values = [0, 2, 5]
    
        for value in values: self.llist.remove_elem_by_index(self.llist.find_first(value))
    
        self.assertEqual(len(self.llist), 10 - len(values))
        self.assertEqual(self.llist, list(set([i for i in range(10)]) - set(values)))

if __name__ == "__main__":
    unittest.main()