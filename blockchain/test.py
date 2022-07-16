import unittest

from user import User
from lib.tree import MerkleTree
from lib.node import Node, Leaf

from lib.utils import digest, digest_double_entries

LEAF_VALUES = ['VALUE1', 'VALUE2', 'VALUE3', 'VALUE4', 'VALUE5', 'VALUES6']
LEAF_HASHES = [digest(value) for value in LEAF_VALUES]
DEPTH = 2
NB_LEAVES = 6
SIZE = 11

class Testnode(unittest.TestCase):
    """
    This test class is used to test methods of the node class
    """
    def test_valid_detached_node(self) -> None:
        """ Test properties of node without relations. """
        node = Node(digest(LEAF_VALUES[0]))

        self.assertEqual(node.left, None)
        self.assertEqual(node.right, None)
        self.assertEqual(node.parent, None)
        self.assertEqual(node.value, digest(LEAF_VALUES[0]))
        self.assertEqual(node.left_count, 0)
        self.assertEqual(node.right_count, 0)
        self.assertEqual(node.is_leaf, False)
        self.assertEqual(node.is_right_child, False)
        self.assertEqual(node.is_left_child, False)
    
    def test_valid_detached_leaf(self) -> None:
        """ Test properties of leaf without relations. """
        leaf = Leaf(digest(LEAF_VALUES[0]))

        self.assertEqual(leaf.left, None)
        self.assertEqual(leaf.right, None)
        self.assertEqual(leaf.parent, None)
        self.assertEqual(leaf.value, digest(LEAF_VALUES[0]))
        self.assertEqual(leaf.left_count, 0)
        self.assertEqual(leaf.right_count, 0)
        self.assertEqual(leaf.is_leaf, True)
        self.assertEqual(leaf.is_right_child, False)
        self.assertEqual(leaf.is_left_child, False)

    def test_node_hash(self) -> None:
        """ Test hashes from node init or leaf bottom-up digest. """
        node = Node(digest_double_entries(digest(LEAF_VALUES[0]), digest(LEAF_VALUES[1])))

        node1 = Node('', Leaf(digest(LEAF_VALUES[0])), Leaf(digest(LEAF_VALUES[1])))
        node1.digest_hashes()

        self.assertEqual(node, node1)
        self.assertEqual(node.value, digest_double_entries(digest(LEAF_VALUES[0]), digest(LEAF_VALUES[1])))
        self.assertEqual(node1.value, digest_double_entries(digest(LEAF_VALUES[0]), digest(LEAF_VALUES[1])))


class TestTree(unittest.TestCase):
    """ 
    This test class is used to test methods of the tree class
    """
    def test_empty_tree(self) -> None:
        """ Test properties of empty tree. """
        bst = MerkleTree()

        self.assertEqual(bst.size, 0)
        self.assertEqual(bst.depth, 0)
        self.assertEqual(bst.nb_leaves, 0)

        self.assertIsNone(bst.hash)
        self.assertIsNone(bst.root)
    
    def test_create_valid_tree(self) -> None:
        """ Test key metrics of valid tree. """
        bst = MerkleTree()

        for value in LEAF_VALUES:
            bst.insert(Leaf(digest(value)))

        self.assertEqual(bst.size, SIZE)
        self.assertEqual(bst.depth, DEPTH)
        self.assertEqual(bst.nb_leaves, len(LEAF_VALUES))

    def test_compare_equal_trees(self) -> None:
        """ Compare that instancing from a list or inserting are equals. """

        bst = MerkleTree()

        for value in LEAF_VALUES:
            bst.insert(Leaf(digest(value)))

        bst1 = MerkleTree(LEAF_VALUES)

        self.assertEqual(bst, bst1)

    def test_hash_tree(self) -> None:
        """ Compare that the hashes are expected. """
        bst = MerkleTree()
        bst.insert(Leaf(digest(LEAF_VALUES[0])))

        self.assertEqual(bst.hash, LEAF_HASHES[0])

        bst.insert(Leaf(digest(LEAF_VALUES[1])))
        self.assertEqual(bst.hash, digest_double_entries(LEAF_HASHES[0], LEAF_HASHES[1]))

if __name__ == '__main__':
    unittest.main()