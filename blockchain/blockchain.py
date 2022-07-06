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

    prev: None | 'Block' = field(init=True)
    next: None | 'Block' = field(init=False, default=None)
    data: dict = field(init=False, default_factory=dict)

@dataclass
class Blockchain:
    """ Chain storing class. """

    current_block: Block = field(init=True)

    def create_block(self):
        raise NotImplementedError()