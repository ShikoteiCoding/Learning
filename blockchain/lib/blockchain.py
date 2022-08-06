from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from .block import Block, Data


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
    tail: Block | None = field(init=False, repr=False, default=None)
    head: Block | None = field(init=False, repr=False, default=None)

    __transaction_queue: list[str] = field(init=False, repr=False, default_factory=list)
    __unspent_outputs: list[UnspentOutput] = field(init=False, repr=False, default_factory=list)

    __nounce: str = field(init=False, default="")
    __size: int = field(init=False, default=0)

    def create_genesis_block(self) -> Block:
        """ Genesis Block. First block. """
        block = Block("", self.__nounce, datetime.now(), Data())
        self.add_block(block.compute_hash())
        return block

    def add_block(self, block: Block) -> Block:
        """ Add a block to existing blockchain. """
        try:
            block.hash
        except (AttributeError) as error:
            raise NotDigestedBlock(f"Block provided has not been hashed yet. {error}")

        if not self.block_is_valid(block):
            raise NotProvedBlock(f"Block provided does not contain proof. Nounce is {self.__nounce}. ")
        
        if not self.tail or not self.head:
            self.tail = block
        else:
            Block.link_blocks(self.head, block)

        self.head = block
        self.__size += 1
        return self.head

    def block_is_valid(self, block: Block) -> bool:
        """ Verify the block hash with the current nounce. """
        return block.hash.startswith(self.__nounce)

    def add_transaction(self, transaction: str) -> None:
        """ Add a transaction in the queue. """
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