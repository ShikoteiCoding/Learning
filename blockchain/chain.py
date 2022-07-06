from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Data:
    """ Data contained in a block. """
    timestamp: datetime = field(init=True, default_factory=datetime.now)
    transactions: str = field(init=True, default="")

@dataclass
class Block:
    """ Block storing class. """

    data: Data = field(init=True)
    signature: str = field(init=True)
    prev: Block = field(init=True, repr=False)
    next: None | Block = field(init=False, default=None, repr=False)

@dataclass
class TailBlock(Block):
    """ Tail block. """

    data: Data = field(init=False, default_factory=Data)
    signature: str = field(init=False, default="")
    prev: None = field(init=False, default=None, repr=False)
    next: None | Block = field(init=False, default=None, repr=False)

@dataclass
class Blockchain:
    """ Chain storing class. """

    tail: TailBlock = field(init=True)
    head: Block = field(init=False)
    _size: int = field(init=False, default=1)

    def __post_init__(self):
        self.head = self.tail

    def forge(self, proof, data, signature) -> dict:
        
        if not proof: return {"message": "refused"}
        
        block = Block(data, signature, self.head)
        self.head.next = block
        self.head = block
        self._size += 1

        return {"message": "success"}
    
    @property
    def size(self) -> int:
        return self._size