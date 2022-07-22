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

    t = "0x3aba4162c7251c891207b747840551a71939b0de081f85c4e44cf7c13e41daa6"
    #t = "0xa966eb6058f8ec9f47074a2faadd3dab42e2c60ed05bc34d39d6c0e1d32b8bdf"
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

    #cprint(pvk_int, pvk_hex, pvk_hex_compressed, pvk_wif, pvk_wif_compressed)
    #cprint(puk_pvk, puk_hex, puk_hex_compressed)
    cprint(add)
    cprint(address_not_compressed, address_compressed)

    print(puk_hex_compressed)
    module = base58.b58encode_check(b'\x00' + bytes.fromhex(puk_hex), alphabet=base58.BITCOIN_ALPHABET)

    cprint(module)
    

if __name__ == "__main__":
    keys()

"""
$ python key-to-address-ecc-example.py
Private Key (hex) is:
 3aba4162c7251c891207b747840551a71939b0de081f85c4e44cf7c13e41daa6
Private Key (decimal) is:
 26563230048437957592232553826663696440606756685920117476832299673293013768870
Private Key (WIF) is:
 5JG9hT3beGTJuUAmCQEmNaxAuMacCTfXuw1R3FCXig23RQHMr4K
Private Key Compressed (hex) is:
 3aba4162c7251c891207b747840551a71939b0de081f85c4e44cf7c13e41daa601
Private Key (WIF-Compressed) is:
 KyBsPXxTuVD82av65KZkrGrWi5qLMah5SdNq6uftawDbgKa2wv6S
Public Key (x,y) coordinates is:
 (41637322786646325214887832269588396900663353932545912953362782457239403430124L,
 16388935128781238405526710466724741593761085120864331449066658622400339362166L)
Public Key (hex) is:
 045c0de3b9c8ab18dd04e3511243ec2952002dbfadc864b9628910169d9b9b00ec243bcefdd4347074d44bd7356d6a53c495737dd96295e2a9374bf5f02ebfc176
Compressed Public Key (hex) is:
 025c0de3b9c8ab18dd04e3511243ec2952002dbfadc864b9628910169d9b9b00ec
Bitcoin Address (b58check) is:
 1thMirt546nngXqyPEz532S8fLwbozud8
Compressed Bitcoin Address (b58check) is:
 14cxpo3MBCYYWCgF74SWTdcmxipnGUsPw3
"""