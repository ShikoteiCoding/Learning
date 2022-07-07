from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Data:
    """ Data contained in a block. """
    transactions: str = field(init=True, default="")

@dataclass
class Block:
    """ Block storing class. """
    previous_hash: str = field(init=True)
    data: Data = field(init=True)
    nounce: str = field(init=True)
    hash: str = field(init=True)

    _prev: Block = field(init=False, repr=False)
    _next: None | Block = field(init=False, default=None, repr=False)

@dataclass
class TailBlock(Block):
    """ Tail block. """
    previous_hash: None | str = field(init=False, default=None)
    data: None | Data = field(init=False, default_factory=Data)
    nounce: str = field(init=False, default="")
    hash: str = field(init=False, default="")

    _prev: None = field(init=False, default=None, repr=False)
    _next: None | Block = field(init=False, default=None, repr=False)

@dataclass
class Blockchain:
    """ Chain storing class. """
    tail: TailBlock = field(init=True)
    head: Block = field(init=False)

    _nounce: str = field(init=False, default="")
    _size: int = field(init=False, default=1)

    def __post_init__(self):
        self.head = self.tail

    def forge(self, block: Block, proof: str) -> dict:
        
        if not proof: return {"message": "refused"}

        block._prev = self.head
        self.head._next = block
        self.head = block
        self._size += 1

        return {"message": "success"}
    
    @property
    def size(self) -> int:
        return self._size

    @property
    def nounce(self) -> str:
        return self._nounce
    @nounce.setter
    def nounce(self, new: str) -> None:
        self._nounce = new

def fake_hash() -> str:
    return ""

def mine_block(previous_hash: str, transactions: str, nounce: str) -> tuple[Block, str]:
    """ Mining encapsulation. Simplistic version waiting for API """
    return Block(previous_hash, Data(transactions), nounce, fake_hash()), "fake proof"