from lib.blockchain import Blockchain
from lib.block import Block, Data

from lib.tree import MerkleTree
from lib.node import Node, Leaf

from lib.utils import digest, digest_double_entries

from datetime import datetime

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
    head = bc.create_genesis_block()

    b1 = bc.add_block(Block(head.hash, "", datetime.now(), Data()).compute_hash())
    b2 = bc.add_block(Block(b1.hash, "", datetime.now(), Data()).compute_hash())

    print(bc)


if __name__ == "__main__":
    create_blockchain_without_users()