import unittest

from lib.user import (
    User, 
    encode_public_key, generate_private_key_from_value, generate_public_key_from_private_key
)
from lib.tree import MerkleTree
from lib.node import Node, Leaf
from fastecdsa.point import Point

from lib.utils import digest, digest_double_entries

LEAF_VALUES = ['VALUE1', 'VALUE2', 'VALUE3', 'VALUE4', 'VALUE5', 'VALUES6']
LEAF_HASHES = [digest(value) for value in LEAF_VALUES]
DEPTH = 2
NB_LEAVES = 6
SIZE = 11

USERS = ['USER1', 'USER2', 'USERS3']

class TestUtilsDigestFunctions(unittest.TestCase):
    """
    This test class is used to test the hash functions used throughout the project.
    """

    def test_hash(self) -> None:
        """ Test the digest functions. """
        value = 'VALUE1'
        hash = digest(value)

        self.assertEqual(len(hash), 64)
        self.assertEqual(hash, 'a19e1a35ea85f3b12c287171db8cdb86d6ddff957ec676cda7fbedadf36873f2')

    def test_hash_pair(self) -> None:
        """ Test the digest functions. """
        hash1 = digest('VALUE1')
        hash2 = digest('VALUE2')

        hash_pair = digest_double_entries(hash1, hash2)

        self.assertEqual(len(hash1), 64)
        self.assertEqual(len(hash2), 64)
        self.assertEqual(len(hash_pair), 64)
        self.assertEqual(hash1, 'a19e1a35ea85f3b12c287171db8cdb86d6ddff957ec676cda7fbedadf36873f2')
        self.assertEqual(hash2, 'fe3d147c5902a7c7e0956b7074527202a4965789669a78478a636108b32c63f4')
        self.assertEqual(hash_pair, 'c2a453d71ede92bf62131122161774fbc05775ccb546dea4642a2472814ef134')

class TestNode(unittest.TestCase):
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

        self.assertIsNone(node.left)
        self.assertIsNone(node.right)
        self.assertIsNone(node.parent)

        self.assertEqual(node.value, digest(LEAF_VALUES[0]))
        self.assertEqual(node.left_count, 0)
        self.assertEqual(node.right_count, 0)

        self.assertFalse(node.is_leaf)
        self.assertFalse(node.is_right_child)
        self.assertFalse(node.is_left_child)
    
    def test_valid_satellite_leaf(self) -> None:
        """ Test properties of leaf without relations. """

        leaf = Leaf(digest(LEAF_VALUES[0]))

        self.assertIsNone(leaf.left)
        self.assertIsNone(leaf.right)
        self.assertIsNone(leaf.parent)

        self.assertEqual(leaf.value, digest(LEAF_VALUES[0]))
        self.assertEqual(leaf.left_count, 0)
        self.assertEqual(leaf.right_count, 0)

        self.assertTrue(leaf.is_leaf)
        self.assertFalse(leaf.is_right_child)
        self.assertFalse(leaf.is_left_child)

    def test_valid_parent_node(self) -> None:
        """ Test properties of node without relations. """

        # Create the leaf children
        left_leaf = Leaf(digest(LEAF_VALUES[0]))
        right_leaf = Leaf(digest(LEAF_VALUES[1]))

        # Create a parent node and digest hashes
        root_node = Node('', left_leaf, right_leaf)
        root_node.digest_hashes()

        # Test node properties
        self.assertIsNone(root_node.parent)

        self.assertEqual(root_node.left, left_leaf)
        self.assertEqual(root_node.right, right_leaf)
        self.assertEqual(root_node.value, digest_double_entries(left_leaf.value, right_leaf.value))
        self.assertEqual(root_node.left_count, 1)
        self.assertEqual(root_node.right_count, 1)

        self.assertFalse(root_node.is_leaf)
        self.assertFalse(root_node.is_right_child)
        self.assertFalse(root_node.is_left_child)

        # Test children properties
        self.assertIsNone(left_leaf.left)
        self.assertIsNone(left_leaf.right)

        self.assertEqual(left_leaf.parent, root_node)
        self.assertEqual(left_leaf.value, digest(LEAF_VALUES[0]))
        self.assertEqual(left_leaf.left_count, 0)
        self.assertEqual(left_leaf.right_count, 0)

        self.assertTrue(left_leaf.is_leaf)
        self.assertFalse(left_leaf.is_right_child)
        self.assertTrue(left_leaf.is_left_child)

        self.assertIsNone(right_leaf.left)
        self.assertIsNone(right_leaf.right)

        self.assertEqual(right_leaf.parent, root_node)
        self.assertEqual(right_leaf.value, digest(LEAF_VALUES[1]))
        self.assertEqual(right_leaf.left_count, 0)
        self.assertEqual(right_leaf.right_count, 0)

        self.assertTrue(right_leaf.is_leaf)
        self.assertTrue(right_leaf.is_right_child)
        self.assertFalse(right_leaf.is_left_child)

class TestMerkleTree(unittest.TestCase):
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

class TestBlock(unittest.TestCase):
    """ 
    This class is used to test things related to the Block of a chain.
    """
    # Not implemented as there will be improvements now that the global architecture is understood.

class TestUser(unittest.TestCase):
    """
    This class is used to test attributes, methods and properties of a potential blockchain User.
    """

    def setUp(self) -> None:
        """
        Initialise a user here as it is an expensive operation and several operations are tested.
        """
        self.username = USERS[0]
        self.user = User(self.username)

        self.private_key = generate_private_key_from_value(self.username)
        self.public_key, self.public_key_encoded = generate_public_key_from_private_key(self.private_key)

        self.user.set_keys(self.private_key, self.public_key, self.public_key_encoded)
    
    def tearDown(self) -> None:
        super().tearDown()

    def test_encoding_functions(self) -> None:
        """ Test the functions stored in user to deal with users keys. """

        private_key = generate_private_key_from_value("VALUE1")

        self.assertGreaterEqual(len(str(private_key)), 64)
        self.assertLessEqual(len(str(private_key)), 78)
        self.assertEqual(private_key, 73101711357121244040869557647379862999364686624517238390144621704807218443250)

        public_key, public_key_encoded = generate_public_key_from_private_key(private_key)
        self.assertEqual(public_key.x, 68863937396896224516328106466925409444047391051799494080204469204999097398252)
        self.assertEqual(public_key.y, 112448337416410614927640030702529231480407343724892916721680495766641425200342)

        # Remove '0x' indicating hexadecimal value
        self.assertEqual(public_key_encoded[2:], '2983f9b7987fd629dadf622093b9743e7f9f62243e79b9924b44798fa6db9b3ec')


    def test_valid_user(self) -> None:
        """
        Test properties and initialisation of a user.
        """

        self.assertEqual(self.user.private_key, self.private_key)
        self.assertEqual(self.user.public_key, self.public_key)
        self.assertEqual(self.user.public_key_encoded, self.public_key_encoded)

    def test_export_import_user(self):
        """
        Test serialization of a user.
        """

        User.export_(self.user)
        imported_user = User.import_(self.username)

        self.assertEqual(imported_user.private_key, self.private_key)
        self.assertEqual(imported_user.public_key, self.public_key)
        self.assertEqual(imported_user.public_key_encoded, self.public_key_encoded)

        self.assertEqual(self.user.private_key, self.private_key)
        self.assertEqual(self.user.public_key, self.public_key)
        self.assertEqual(self.user.public_key_encoded, self.public_key_encoded)


if __name__ == '__main__':
    unittest.main()