from chain import Blockchain, Block, Data, TailBlock, mine_block

def create_block_chain_without_users():
    """ Create and build blockchain without users. Simplistic scenario. """

    bc = Blockchain(TailBlock())
    first_block, first_proof = mine_block(bc.head.hash, "transactions first block", bc.nounce)
    print(bc.forge(first_block, first_proof))
    scd_block, scd_proof = mine_block(bc.head.hash, "transactions scd block", bc.nounce)
    print(bc.forge(scd_block, scd_proof))

    print(bc)

if __name__ == "__main__":
    create_block_chain_without_users()