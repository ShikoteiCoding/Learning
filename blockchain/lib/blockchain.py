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
    def prev(self) -> None | Block:
        return self.__prev

    @prev.setter
    def prev(self, prev_block: Block) -> None:
        if prev_block.hash != self.previous_hash: 
            raise WrongBlockError(f"Hash are not corresponding: {self.previous_hash} and {prev_block.hash}")
        self.__prev = prev_block

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
    tail: Block | None = field(init=False, default=None)
    head: Block | None = field(init=False, default=None)

    __nounce: str = field(init=False, default="")
    __size: int = field(init=False, default=1)

    def create_genesis_block(self):
        """ Genesis Block. First block. """
        block = Block("", self.__nounce, datetime.now(), Data(""))
        block.hash = block.compute_hash()
        self.__append_block(block)
    
    def __append_block(self, block: Block) -> None:
        if not self.block_is_valid(block):
            return
        
        if not self.tail:
            self.tail = block
            self.head = block
            return
        
        self.head = block

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