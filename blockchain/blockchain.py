from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Data:
    """ Data contained in a block. """
    timestamp: datetime
    proof: str
    signature: str

@dataclass
class Block:
    """ Block storing class. """

    data: dict = field(init=True)
    signature: str = field(init=True)
    prev: 'Block' = field(init=True)
    next: None | 'Block' = field(init=False, default=None)

@dataclass
class Blockchain:
    """ Chain storing class. """

    tail: Block = field(init=True)
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