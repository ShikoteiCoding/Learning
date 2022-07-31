from lib.blockchain import Blockchain
from lib.block import Block, Data

from lib.tree import MerkleTree
from lib.node import Node, Leaf
from lib.user import ( User, 
    generate_private_key_from_value, generate_public_key_from_private_key, generate_address_from_public_key
)

from lib.utils import digest, digest_double_entries, cprint, encode_elliptic_point, hash160
from lib.keys import PrivateKey, PublicKey, Address
from fastecdsa.point import Point

import base58

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

def keys() -> None:

    t = "0x3aba4162c7251c891207b747840551a71939b0de081f85c4e44cf7c13e41daa6"
    pu_key_point = generate_public_key_from_private_key(int(t, base=16))

    pvk_int = PrivateKey(t)
    pvk_hex = pvk_int.hex()
    pvk_hex_compressed = pvk_int.hex(compressed=True)
    pvk_wif = pvk_int.wif()
    pvk_wif_compressed = pvk_int.wif(compressed=True)

    puk_pvk = PublicKey(pvk_int)
    puk_hex = puk_pvk.hex()
    puk_hex_compressed = puk_pvk.hex(compressed=True)

    add = Address(puk_pvk)
    address_not_compressed = "1thMirt546nngXqyPEz532S8fLwbozud8"
    address_compressed = "14cxpo3MBCYYWCgF74SWTdcmxipnGUsPw3"
    cprint(add)
    cprint(address_not_compressed, address_compressed)

    print(puk_hex_compressed)
    module = base58.b58encode_check(b'\x00' + bytes.fromhex(puk_hex), alphabet=base58.BITCOIN_ALPHABET)

    cprint(module)

def create_users() -> None:
    user = User("User-1", PrivateKey("0x3aba4162c7251c891207b747840551a71939b0de081f85c4e44cf7c13e41daa6"))

    cprint(
        user
    )

    

if __name__ == "__main__":
    create_users()