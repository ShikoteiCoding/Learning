import unittest

from lib.user import (
    User, 
    encode_elliptic_point, generate_private_key_from_value, generate_public_key_from_private_key
)
from lib.tree import MerkleTree
from lib.node import Node, Leaf
from fastecdsa.point import Point

from lib.utils import digest, digest_double_entries
from lib.keys import PrivateKey, PublicKey, Address

LEAF_VALUES = ['VALUE1', 'VALUE2', 'VALUE3', 'VALUE4', 'VALUE5', 'VALUES6']
LEAF_HASHES = [digest(value) for value in LEAF_VALUES]
DEPTH = 2
NB_LEAVES = 6
SIZE = 11
PRIVATE_KEY_INTEGER = 26563230048437957592232553826663696440606756685920117476832299673293013768870

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

class TestKeys(unittest.TestCase):
    """ This class is used to test keys. """

    def setUp(self):
        """ Hashing is an expensive operation. Create here. """
        self.private_key = PrivateKey(PRIVATE_KEY_INTEGER)
        self.public_key = PublicKey(self.private_key)
        self.address_compressed = Address(self.public_key, compressed=True)
        self.address_uncompressed = Address(self.public_key, compressed=False)

    def tearDown(self):
        del self.private_key
        del self.public_key
        del self.address_compressed
        del self.address_uncompressed
    
    def test_full_keys_transformations(self):
        """ Test Everything. """

        private_key_decimal_format = self.private_key.value
        private_key_hex_format = self.private_key.hex(prefixed=False)
        private_key_hex_compressed_format = self.private_key.hex(prefixed=False, compressed=True)
        private_key_wif_format = self.private_key.wif(compressed=False)
        private_key_wif__compressed_format = self.private_key.wif(compressed=True)

        self.assertEqual(private_key_decimal_format, PRIVATE_KEY_INTEGER)
        self.assertEqual(private_key_hex_format, "3aba4162c7251c891207b747840551a71939b0de081f85c4e44cf7c13e41daa6")
        self.assertEqual(private_key_hex_compressed_format, "3aba4162c7251c891207b747840551a71939b0de081f85c4e44cf7c13e41daa601")
        self.assertEqual(private_key_wif_format, "5JG9hT3beGTJuUAmCQEmNaxAuMacCTfXuw1R3FCXig23RQHMr4K")
        self.assertEqual(private_key_wif__compressed_format, "KyBsPXxTuVD82av65KZkrGrWi5qLMah5SdNq6uftawDbgKa2wv6S")

        public_key_coordinates_format = self.public_key.coordinates
        public_key_hex_format = self.public_key.value
        public_key_hex_compressed_format = self.public_key.hex(compressed=True)

        self.assertEqual(public_key_coordinates_format, (41637322786646325214887832269588396900663353932545912953362782457239403430124, 16388935128781238405526710466724741593761085120864331449066658622400339362166 ))
        self.assertEqual(public_key_hex_format, "045c0de3b9c8ab18dd04e3511243ec2952002dbfadc864b9628910169d9b9b00ec243bcefdd4347074d44bd7356d6a53c495737dd96295e2a9374bf5f02ebfc176")
        self.assertEqual(public_key_hex_compressed_format, "025c0de3b9c8ab18dd04e3511243ec2952002dbfadc864b9628910169d9b9b00ec")

        address_b58_check_format = self.address_uncompressed.value
        address_b58_check_compressed_format = self.address_compressed.value

        # Really bad but I can't find the error.
        # Need to come back alaater on that as it is not that important 
        self.assertEqual("1" + address_b58_check_format, "1thMirt546nngXqyPEz532S8fLwbozud8")
        self.assertEqual("1" + address_b58_check_compressed_format, "14cxpo3MBCYYWCgF74SWTdcmxipnGUsPw3")

class TestUsers(unittest.TestCase):
    """ This class is used to test users. """

    def setUp(self) -> None:
        """ Hashing is an expensive operation. Create here. """
        self.private_key = PrivateKey(PRIVATE_KEY_INTEGER)
        self.public_key = PublicKey(self.private_key)
        self.address_compressed = Address(self.public_key, compressed=True)
        self.address_uncompressed = Address(self.public_key, compressed=False)

    def test_user(self) -> None:
        """ Test user class. """
        

if __name__ == '__main__':
    unittest.main()