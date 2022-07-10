from lib.blockchain import Blockchain, TailBlock, mine_block

from lib.tree import MerkleTree

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
    bst.insert("hahade")
    print(bst)
    bst.insert("hahaded")
    print(bst)
    bst.insert("haddhaded")
    print(bst)
    bst.insert("haddhaded")
    print(bst)

if __name__ == "__main__":
    insert_in_binary_tree()