from __future__ import annotations

from dataclasses import InitVar, dataclass, field
from datetime import datetime

from .block import Block, Data
from .transaction import Transaction


class NotDigestedBlock(Exception):
    ...
class NotProvedBlock(Exception):
    ...

@dataclass
class UnspentOutput:
    """
    Output of a transaction to store global latest state.
    Each participant (buyer + sellers) should produce an output.
    Used to verified if the transaction is possible.
    """
    transaction_hash: str
    transaction_index: int
    transaction_output_index: int
    value: int
    value_hex: str

@dataclass
class Blockchain:
    """ Chain storing class. """
    genesis_block: InitVar[Block]
    genesis_nounce: InitVar[str]

    tail: Block = field(init=False, repr=False)
    head: Block = field(init=False, repr=False)

    __nounce: str = field(init=False, repr=True)
    __size: int = field(init=False, repr=True, default=0)

    __transaction_queue: list[Transaction] = field(init=False, repr=False, default_factory=list)
    __validated_transactions: list[Transaction] = field(init=False, default_factory=list)
    __unspent_outputs: list[UnspentOutput] = field(init=False, repr=False, default_factory=list)

    def __post_init__(self, genesis_block: Block, genesis_nounce: str) -> None:
        """ Initializing the blockchain given a pre-forged block. """
        self.__nounce = genesis_nounce
        self.tail = genesis_block
        self.head = genesis_block
        self.__size = 1

    @staticmethod  
    def create_genesis_block(nounce: str) -> Block:
        """ Genesis Block. First block. """
        block = Block("", nounce, datetime.now(), Data())
        return block
    
    @staticmethod
    def block_voting(mined_blocks: list[Block]):
        """ Given many blocks, select the first correct mined block. """
        raise NotImplementedError()

    def add_block(self, block: Block) -> Block:
        """ Add a block to existing blockchain. """
        try:
            block.hash
        except (AttributeError) as error:
            raise NotDigestedBlock(f"Block provided has not been hashed yet. {error}")

        if not self.block_is_valid(block):
            raise NotProvedBlock(f"Block provided does not contain proof. Nounce is {self.__nounce}. ")
        
        Block.link_blocks(self.head, block)

        self.head = block
        self.__size += 1
        return self.head

    def block_is_valid(self, block: Block) -> bool:
        """ Verify the block hash with the current nounce. """
        return block.hash.startswith(self.__nounce)

    def add_transaction(self, transaction: Transaction) -> None:
        """ Add a transaction in the queue. Transaction is considered to be valid at this point. """
        self.__transaction_queue.append(transaction)

    def mine(self) -> None:
        if not self.__transaction_queue:
            return 
        
        last_block = self.last_block

        if not last_block: return

        block = Block(
            last_block.hash,
            self.__nounce,
            datetime.now(),
            Data(str(self.__transaction_queue))
        ).compute_hash()

        self.add_block(block)
        self.__transaction_queue = []

    @property
    def last_block(self) -> Block | None:
        return self.head
    
    @property
    def size(self) -> int:
        return self.__size

    @property
    def nounce(self) -> str:
        return self.__nounce

    @nounce.setter
    def nounce(self, nounce: str) -> None:
        self.__nounce = nounce

    def __str__(self) -> str:
        out = ""
        curr = self.tail
        counter = 0
        while curr:
            out += f"\nBlock {counter}: {curr.hash}"
            counter += 1
            curr = curr.next
        return out