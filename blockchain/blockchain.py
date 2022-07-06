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
    prev: 'Block' = field(init=True)
    next: None | 'Block' = field(init=False, default=None)

@dataclass
class TailBlock(Block):
    """ Tail block. """

    data: Data = field(init=False, default_factory=Data)
    signature: str = field(init=False, default="")
    prev: None = field(init=False, default=None)
    next: None | 'Block' = field(init=False, default=None)

@dataclass
class Blockchain:
    """ Chain storing class. """

    tail: TailBlock = field(init=True)
    head: Block = field(init=False)
    _size: int = field(init=False, default=0)

    def forge(self, proof, data, signature) -> dict:
        
        if not proof: return {"message": "refused"}
        
        block = Block(data, signature, self.head)
        self.head.next = block
        self.head = block

        return {"message": "success"}
    
    @property
    def size(self) -> int:
        return self._size