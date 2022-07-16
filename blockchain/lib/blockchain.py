from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

class WrongBlockError(Exception):
    ...

@dataclass
class Data:
    """ Data contained in a block. """
    # Should it be where  the merkle tree is placed ?
    # Need further documentation
    transactions: str = field(init=True, default="")

@dataclass(slots=True)
class Block:
    """ Block storing class. """

    previous_hash: str  = field(init=True)
    nounce: str         = field(init=True)    # Starting string of the hash (used to virtually confirm work proof)
    timestamp: datetime = field(init=True)
    data: Data          = field(init=True)

    __hash: str = field(init=False)

    __prev: Block | None = field(init=False, repr=False, default=None)
    __next: Block | None = field(init=False, repr=False, default=None)

    @property
    def prev(self) -> Block | None:
        return self.__prev

    @prev.setter
    def prev(self, block: Block | None) -> None:
        if block:
            if block.hash != self.previous_hash: 
                raise WrongBlockError(f"Hash are not corresponding: {self.previous_hash} and {block.hash}")
        self.__prev = block

    @property
    def next(self) -> Block | None:
        return self.__next
    
    @next.setter
    def next(self, block: Block | None) -> None:
        self.__next = block

    @property
    def hash(self) -> str:
        return self.__hash

    @hash.setter
    def hash(self, hash: str) -> None:
        self.__hash = hash

    def compute_hash(self):
        return ""

@dataclass
class Blockchain:
    """ Chain storing class. """
    tail: Block | None = field(init=False, repr=False, default=None)
    head: Block | None = field(init=False, repr=False, default=None)

    __nounce: str = field(init=False, default="")
    __size: int = field(init=False, default=0)

    def create_genesis_block(self):
        """ Genesis Block. First block. """
        block = Block("", self.__nounce, datetime.now(), Data(""))
        block.hash = block.compute_hash()
        self.__append_block(block)
    
    def __append_block(self, block: Block) -> None:
        if not self.block_is_valid(block):
            return
        
        if not self.tail or not self.head:
            self.tail = block
            self.head = block
            return
        
        self.head.next = block
        block.prev = self.head
        self.head = block

        self.__size += 1

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