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
    This test class is used to test methods of the node class.
    """

    def test_valid_satellite_node(self) -> None:
        """ 
        Test properties of node without relations. 
        Note: that a satellite node should not exist in a tree, a node without children is a leaf.
        This testing purposes as leaf and node shares inherited behaviour.
        """

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
    
    def test_valid_satellite_leaf(self) -> None:
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

    def test_valid_parent_node(self) -> None:
        """ Test properties of node without relations. """

        # Create the leaf children
        left_leaf = Leaf(digest(LEAF_VALUES[0]))
        right_leaf = Leaf(digest(LEAF_VALUES[1]))

        # Create a parent node and digest hashes
        root_node = Node('', left_leaf, right_leaf)
        root_node.digest_hashes()

        # Test node properties
        self.assertEqual(root_node.left, left_leaf)
        self.assertEqual(root_node.right, right_leaf)
        self.assertEqual(root_node.parent, None)
        self.assertEqual(root_node.value, digest_double_entries(left_leaf.value, right_leaf.value))
        self.assertEqual(root_node.left_count, 1)
        self.assertEqual(root_node.right_count, 1)
        self.assertEqual(root_node.is_leaf, False)
        self.assertEqual(root_node.is_right_child, False)
        self.assertEqual(root_node.is_left_child, False)

        # Test children properties
        self.assertEqual(left_leaf.left, None)
        self.assertEqual(left_leaf.right, None)
        self.assertEqual(left_leaf.parent, root_node)
        self.assertEqual(left_leaf.value, digest(LEAF_VALUES[0]))
        self.assertEqual(left_leaf.left_count, 0)
        self.assertEqual(left_leaf.right_count, 0)
        self.assertEqual(left_leaf.is_leaf, True)
        self.assertEqual(left_leaf.is_right_child, False)
        self.assertEqual(left_leaf.is_left_child, True)

        self.assertEqual(right_leaf.left, None)
        self.assertEqual(right_leaf.right, None)
        self.assertEqual(right_leaf.parent, root_node)
        self.assertEqual(right_leaf.value, digest(LEAF_VALUES[1]))
        self.assertEqual(right_leaf.left_count, 0)
        self.assertEqual(right_leaf.right_count, 0)
        self.assertEqual(right_leaf.is_leaf, True)
        self.assertEqual(right_leaf.is_right_child, True)
        self.assertEqual(right_leaf.is_left_child, False)

    def test_node_hash(self) -> None:
        """ Test hashes from node init or leaf bottom-up digest. """
        # Define a node without children but a hash (just for testing)
        detached_node = Node(digest_double_entries(digest(LEAF_VALUES[0]), digest(LEAF_VALUES[1])))

        # Define a node with leaf children and digest the bottom-up hashes
        parent_node = Node('', Leaf(digest(LEAF_VALUES[0])), Leaf(digest(LEAF_VALUES[1])))
        parent_node.digest_hashes()

        self.assertEqual(detached_node, parent_node)
        self.assertEqual(detached_node.value, digest_double_entries(digest(LEAF_VALUES[0]), digest(LEAF_VALUES[1])))
        self.assertEqual(parent_node.value, digest_double_entries(digest(LEAF_VALUES[0]), digest(LEAF_VALUES[1])))


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