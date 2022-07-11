import unittest

from user import User
from lib.tree import MerkleTree

NODE_VALUES = ['VALUE1', 'VALUE2', 'VALUE3', 'VALUE4', 'VALUE5']

class TestUsers(unittest.TestCase):

    def create_user(self) -> None:
        """ Test users needed attribute to perform transactions. """
        user = User()


class TestTree(unittest.TestCase):
    
    def create_valid_tree(self) -> None:
        """ Test key metrics of valid tree. """
        bst = MerkleTree()

        for value in NODE_VALUES:
            bst.insert(value)

        self.assertEqual(bst.size, len(NODE_VALUES) + 10)

if __name__ == '__main__':
    unittest.main()