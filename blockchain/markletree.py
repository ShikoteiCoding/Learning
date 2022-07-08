from __future__ import annotations
from dataclasses import InitVar, dataclass, field

import hashlib

def hash(value: str) -> str:
    """ Hash a string value. """
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

@dataclass
class Node:
    """ Node sub-element of Markle Tree """
    value: str = field(init=True, repr=True, default="")
    right: Node | None = field(init=True, repr=False, default=None)
    left: Node | None = field(init=True, repr=False, default=None)

@dataclass
class BinaryTree:
    """ Data Structure holding hashed transactions. """

    values: InitVar[list[str]]

    root: Node = field(init=False, repr=True, default_factory=Node)
    size: int = field(init=False, repr=True, default=0)

    def __post_init__(self, values: list[str]) -> None:
        """ Build the tree from list of values. """

        nodes: list[Node] = [Node(hash(value)) for value in values]

        self.root = self.__build_tree_recursive(nodes)

    def __build_tree_recursive(self, nodes: list[Node]) -> Node:
        """ Recursively build the nodes and their descendants. """

        half: int = len(nodes) // 2

        if len(nodes) == 2:
            return Node(hash(nodes[0].value + nodes[1].value), nodes[0], nodes[1])
        if len(nodes) == 1:
            return Node(hash(nodes[0].value), nodes[0])

        left: Node = self.__build_tree_recursive(nodes[:half])
        right: Node = self.__build_tree_recursive(nodes[half:])
        value: str = hash(left.value + right.value)

        return Node(value, left, right)

    def add(self, value: str) -> None:
        """ Add a leaf to the tree. """
        raise NotImplementedError()

    def print_tree(self) -> None:
        self.__print_tree_recursive(self.root)

    def __print_tree_recursive(self, node: Node | None) -> None:
        if node != None:
            print(node.value)
            self.__print_tree_recursive(node.right)
            self.__print_tree_recursive(node.left)

    @property
    def hash(self):
        return self.root.value