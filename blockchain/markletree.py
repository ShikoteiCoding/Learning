from __future__ import annotations
from dataclasses import InitVar, dataclass, field

import hashlib

MAX_ELEMENT = 10

def hash(key: str) -> str:
    return hashlib.sha256(key.encode('utf-8')).hexdigest()

@dataclass
class Node:
    """ Node sub-element of Markle Tree """
    value: str = field(init=True, repr=True, default="")
    right: Node | None = field(init=False, repr=False, default=None)
    left: Node | None = field(init=False, repr=False, default=None)

@dataclass
class BinaryTree:
    """ Data Structure holding hashed transactions. """

    values: InitVar[list[str]]

    head: Node = field(init=False, repr=True, default_factory=Node)
    size: int = field(init=False, repr=True, default=0)

    def __post_init__(self, values: list[str]) -> None:
        """ Build the tree from list of values. """
        print(values)


    def add(self, value: str):
        """ Add a node to the tree """
        index = hash(value) 