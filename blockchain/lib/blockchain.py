from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from .block import Block, Data

class NotDigestedBlock(Exception):
    ...
class NotProvedBlock(Exception):
    ...

@dataclass
class Blockchain:
    """ Chain storing class. """
    tail: Block | None = field(init=False, repr=False, default=None)
    head: Block | None = field(init=False, repr=False, default=None)

    __nounce: str = field(init=False, default="")
    __size: int = field(init=False, default=0)

    def create_genesis_block(self) -> Block:
        """ Genesis Block. First block. """
        block = Block("", self.__nounce, datetime.now(), Data(""))
        self.__append_block(block.compute_hash())
        return block

    def add_block(self, block: Block) -> Block:
        """ Add a block to existing blockchain. """
        try:
            block.hash
        except (AttributeError) as error:
            raise NotDigestedBlock(f"Block provided has not been hashed yet. {error}")
        return self.__append_block(block)
    
    def __append_block(self, block: Block) -> Block:
        if not self.block_is_valid(block):
            raise NotProvedBlock(f"Block provided does not contain proof. Nounce is {self.__nounce}. ")
        
        if not self.tail or not self.head:
            self.tail = block
            self.head = block
            return self.head
        
        Block.link_blocks(self.head, block)

        self.head = block
        self.__size += 1

        return self.head

    def block_is_valid(self, block: Block) -> bool:
        """ Verify the block hash with the current nounce. """
        return block.hash.startswith(self.__nounce)
    
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