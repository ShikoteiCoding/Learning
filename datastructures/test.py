import unittest

from arrays import (Stack, Queue)

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

if __name__ == "__main__":
    unittest.main()