from __future__ import annotations

from dataclasses import dataclass, field

from datetime import datetime
from .utils import digest

class WrongBlockLinkError(Exception):
    ...

@dataclass(slots=True)
class Data:
    """ Data contained in a block. """
    # Should it be where  the merkle tree is placed ?
    # Need further documentation
    transactions: str = field(init=True, default="")

    def __str__(self) -> str:
        return self.transactions

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

    @staticmethod
    def link_blocks(prev_block: Block, next_block: Block) -> None:
        """ Link blocks between them. """
        prev_block.next = next_block
        next_block.prev = prev_block

    @property
    def prev(self) -> Block | None:
        return self.__prev

    @prev.setter
    def prev(self, block: Block | None) -> None:
        if block:
            if block.hash != self.previous_hash: 
                raise WrongBlockLinkError(f"Hash are not corresponding: {self.previous_hash} and {block.hash}")
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

    def compute_hash(self) -> Block:
        self.__hash = digest(self.previous_hash + self.nounce + str(self.timestamp) + str(self.data))
        return self