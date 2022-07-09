from __future__ import annotations
from dataclasses import InitVar, dataclass, field

import hashlib

L_BRACKET_SHORT = '└─'
L_BRACKET_LONG = '└──'
T_BRACKET = '├──'
VERTICAL_BAR = '│'

def hash(value: str) -> str:
    """ Hash a string value. """
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

@dataclass
class Node:
    """ Node sub-element of Markle Tree """
    __value: str = field(init=True, repr=True, default="")
    __right: Node | None = field(init=True, repr=False, default=None)
    __left: Node | None = field(init=True, repr=False, default=None)

    @property
    def value(self) -> str:
        """ The hash stored by the node. """
        return self.__value

    @property
    def right(self) -> Node | None:
        """ The right child of the node. """
        return self.__right

    @property
    def left(self) -> Node | None:
        """ The left chiled of the node. """
        return self.__left

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

    def __str__(self, depth: int = 0, indent: int = 3) -> str:
        """ Pretty print of tree. """

        out = self.__to_string_recursive(self.root)
        return out

    def __to_string_recursive(
        self, 
        node: Node, 
        depth: int = 0, 
        indent: int = 3,
        ignored: list = [],
        is_right: bool = False, 
        is_left: bool = False
        ) -> str:

        out: str = ''

        if depth == 0:
            out = '\n' + f'{L_BRACKET_SHORT}'
        else:
            out = ' ' * (indent + 1)

        count = 1
        while count < depth:
            out += f' {VERTICAL_BAR}' if count not in ignored else 2 * ' '
            out += indent * ' '
            count += 1

        if is_left:
            out += f' {T_BRACKET}'
        if is_right:
            out += f' {L_BRACKET_LONG}'
            ignored.append(depth)
        
        out += f"{node.value}\n"

        args = (depth + 1, indent, ignored.copy())

        if node.left:
            out += self.__to_string_recursive(node.left, *args, is_left=True)
        if node.right:
            out += self.__to_string_recursive(node.right, *args, is_right=True)

        return out

    def add(self, value: str) -> None:
        """ Add a leaf to the tree. """
        raise NotImplementedError()

    def find_value(self, value: str) -> None:
        """ Find a node and returns it's position. """
        raise NotImplementedError()

    def find_hash(self, hash: str) -> None:
        raise NotImplementedError()

    @property
    def hash(self):
        return self.root.value