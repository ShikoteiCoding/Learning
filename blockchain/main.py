from chain import Blockchain, Block, Data, TailBlock

def create_block_chain_without_users():
    """ Create and build blockchain without users. Simplistic scenario. """

    bc = Blockchain(TailBlock())
    print(bc)

if __name__ == "__main__":
    create_block_chain_without_users()