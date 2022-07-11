import unittest

from user import User
from lib.tree import MerkleTree

NODE_VALUES = ['VALUE1', 'VALUE2', 'VALUE3', 'VALUE4', 'VALUE5']
DEPTH = 2
NB_LEAVES = 3

class TestTree(unittest.TestCase):
    """ 
    This test class is used to test methods of the tree class
    """
    
    def test_create_valid_tree(self) -> None:
        """ Test key metrics of valid tree. """
        bst = MerkleTree()

        for value in NODE_VALUES:
            bst.insert(value)

        self.assertEqual(bst.size, len(NODE_VALUES))
        self.assertEqual(bst.depth, DEPTH)
        self.assertEqual(bst.nb_leaves, NB_LEAVES)

if __name__ == '__main__':
    unittest.main()