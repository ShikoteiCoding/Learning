from __future__ import annotations
from dataclasses import dataclass, field

MAX_ELEMENT = 10

def hashcode(key: int) -> int:
    return key % MAX_ELEMENT

# https://www.geeksforgeeks.org/introduction-to-merkle-tree/
@dataclass
class Node:
    """ Node sub-element of Markle Tree """
    key: int = field(init=True, repr=True, default=0)
    value: int = field(init=True, repr=True, default=0)
    right: Node | None = field(init=False, repr=False, default=None)
    left: Node | None = field(init=False, repr=False, default=None)

@dataclass
class BinaryTree:
    """ Data Structure holding hashed transactions. """
    head: Node = field(init=False, repr=True, default_factory=Node)
    size: int = field(init=False, repr=True, default=0)

    def add(self, key: int, value: int):
        """ Add a node to the tree """
        index = hashcode(key)