from lib.blockchain import Blockchain, TailBlock, mine_block

from lib.tree import MerkleTree
from lib.node import Node, Leaf

from lib.utils import hash, hash_entries

from inspect import signature

def create_block_chain_without_users():
    """ Create and build blockchain without users. Simplistic scenario. """

    bc = Blockchain(TailBlock())
    first_block, first_proof = mine_block(bc.head.hash, "transactions first block", bc.nounce)
    print(bc.forge(first_block, first_proof))
    scd_block, scd_proof = mine_block(bc.head.hash, "transactions scd block", bc.nounce)
    print(bc.forge(scd_block, scd_proof))

    print(bc)

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

    for val in ['VALUE1', 'VALUE2', 'VALUE3', 'VALUE4', 'VALUE5', 'VALUE6']:
        bst.insert_old(Leaf(hash(val)))
        #print("Old version of inserting:", bst)
        bst1.insert(Leaf(val))
        print("New version of inserting:", bst1)

    print(bst == bst1)

def some_leaves():

    bst1 = MerkleTree()

    for val in ['VALUE1', 'VALUE2', 'VALUE3', 'VALUE4', 'VALUE5', 'VALUE6']:
        print("Insert:", bst1)
        bst1.insert_old(Leaf(hash(val)))

    print("Last:", bst1)

def node_compare():

    LEAF_VALUES = ['VALUE1', 'VALUE2']

    node = Node(hash_entries(hash(LEAF_VALUES[0]), hash(LEAF_VALUES[1])))

    node1 = Node('', Leaf(hash(LEAF_VALUES[0])), Leaf(hash(LEAF_VALUES[1])))
    node1.compute_hash()

    print(node, node1)

if __name__ == "__main__":
    some_tree_metrics()