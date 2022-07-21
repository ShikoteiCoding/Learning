from lib.blockchain import Blockchain
from lib.block import Block, Data

from lib.tree import MerkleTree
from lib.node import Node, Leaf
from lib.user import ( User, 
    generate_private_key_from_value, generate_public_key_from_private_key, generate_address_from_public_key
)

from lib.utils import digest, digest_double_entries, cprint, encode_elliptic_point
from lib.keys import PrivateKey, PublicKey
from fastecdsa.point import Point

DATA_PATH = 'data/'

def create_hashed_binary_tree():
    """ Create a binary tree from arbitrary list of data. """
    
    bst = MerkleTree(["salut", "i'm", "an", "anus", "abab", "jdj", "sas", "sass", "askas", "adzad"])

def insert_in_binary_tree():

    bst = MerkleTree()
    bst.insert_old(Leaf("hahade"))
    print(bst)
    bst.insert_old(Leaf("hahaded"))
    print(bst)
    bst.insert_old(Leaf("haddhaded"))
    print(bst)
    bst.insert_old(Leaf("haddhaded"))
    print(bst)

def some_tree_metrics():

    bst1 = MerkleTree()
    bst = MerkleTree()

    for val in ['VALUE1', 'VALUE2', 'VALUE3', 'VALUE4', 'VALUE5', 'VALUE6', 'VALUE7']:
        bst.insert_old(Leaf(digest(val)))
        bst1.insert(Leaf(digest(val)))
        print("New version of inserting:", bst1)

    print(bst == bst1)

def some_leaves():

    bst1 = MerkleTree()

    for val in ['VALUE1', 'VALUE2', 'VALUE3', 'VALUE4', 'VALUE5', 'VALUE6']:
        print("Insert:", bst1)
        bst1.insert_old(Leaf(digest(val)))

    print("Last:", bst1)

def node_compare():

    LEAF_VALUES = ['VALUE1', 'VALUE2']

    node = Node(digest_double_entries(digest(LEAF_VALUES[0]), digest(LEAF_VALUES[1])))

    node1 = Node('', Leaf(digest(LEAF_VALUES[0])), Leaf(digest(LEAF_VALUES[1])))
    node1.digest_hashes()

    print(node, node1)

def create_blockchain_without_users():
    """ Create and build blockchain without users. Simplistic scenario. """

    bc = Blockchain()
    bc.create_genesis_block()

    for _ in range(0, 5):
        bc.add_transaction("I'm a transaction")
        bc.mine()
    
    print(bc)

def create_users() -> None:
    user = User.import_("User 1")

    private_key = generate_private_key_from_value("VALUE1")
    public_key, public_key_encoded = generate_public_key_from_private_key(private_key)
    address = generate_address_from_public_key(public_key_encoded)

    cprint(
        private_key,
        public_key,
        public_key_encoded,
        address,
    )
    print(len(public_key_encoded))
    print(len('0202a406624211f2abbdc68da3df929f938c3399dd79fac1b51b0e4ad1d26a47aa'))

def keys() -> None:

    pv_key_hex = "0x1E99423A4ED27608A15A2616A2B0E9E52CED330AC530EDCC32C8FFC6A526AEDD"
    pu_key_point = generate_public_key_from_private_key(int(pv_key_hex, base=16))

    pvk_int = PrivateKey(pv_key_hex)
    print(pu_key_point)

    puk_pvk = PublicKey(pvk_int)

    cprint(pvk_int, puk_pvk)

    #cprint(pv_key_hex, pvk_int, pvk_hex, pvk_wif)
    

if __name__ == "__main__":
    keys()