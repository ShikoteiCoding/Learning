import unittest

from user import User
from lib.tree import MerkleTree
from lib.node import Leaf

from lib.utils import hash

NODE_VALUES = ['VALUE1', 'VALUE2', 'VALUE3', 'VALUE4', 'VALUE5', 'VALUES6']
DEPTH = 2
NB_LEAVES = 3

class TestTree(unittest.TestCase):
    """ 
    This test class is used to test methods of the tree class
    """
    def test_empty_tree(self) -> None:
        """ Test metrics and method of empty tree. """
        bst = MerkleTree()

        self.assertEqual(bst.size, 0)
        self.assertEqual(bst.depth, 0)
        self.assertEqual(bst.nb_leaves, 0)

        self.assertIsNone(bst.hash)
        self.assertIsNone(bst.root)
    
    def test_create_valid_tree(self) -> None:
        """ Test key metrics of valid tree. """
        bst = MerkleTree()

        for value in NODE_VALUES:
            bst.insert(Leaf(hash(value)))

        self.assertEqual(bst.size, len(NODE_VALUES))
        self.assertEqual(bst.depth, DEPTH)
        self.assertEqual(bst.nb_leaves, NB_LEAVES)

    def test_compare_init_insert(self) -> None:
        """ Compare that instancing from a list or inserting produce same result. """

        bst = MerkleTree()

        for value in NODE_VALUES:
            bst.insert(Leaf(hash(value)))

        bst1 = MerkleTree(NODE_VALUES)

        self.assertEqual(bst, bst1)

if __name__ == '__main__':
    unittest.main()