from dataclasses import InitVar, dataclass, field
from .node import Node

import hashlib

L_BRACKET_SHORT = '└─'
L_BRACKET_LONG = '└──'
T_BRACKET = '├──'
VERTICAL_BAR = '│'

def hash(value: str) -> str:
    """ Hash a string value. """
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

@dataclass
class MerkleTree:
    """ Data Structure holding hashed transactions. """

    values: InitVar[list[str] | None] = None

    __root: Node | None = field(init=False, repr=True, default_factory=Node)
    __size: int = field(init=False, repr=True, default=0)

    def __post_init__(self, values: list[str] | None) -> None:
        """ Build the tree from list of values. """

        if not values: return
        
        nodes: list[Node] = [Node(hash(value)) for value in values]
        self.__root = self.__build_tree_recursive(nodes)

    def __build_tree_recursive(self, nodes: list[Node]) -> Node:
        """ Recursively build the nodes and their descendants. """

        half: int = len(nodes) // 2

        if len(nodes) == 2:
            return Node(hash(nodes[0].value + nodes[1].value), nodes[0], nodes[1])
        if len(nodes) == 1:
            return Node(hash(nodes[0].value), nodes[0])

        left: Node = self.__build_tree_recursive(nodes[half:])
        right: Node = self.__build_tree_recursive(nodes[:half])
        value: str = hash(left.value + right.value)

        return Node(value, left, right)

    def __str__(self) -> str | None:
        """ Pretty print of tree. """

        if not self.__root: return

        return self.__to_string_recursive(self.__root)

    def __to_string_recursive(self, node: Node, depth: int = 0, indent: int = 3, 
            ignored: list = [], is_right: bool = False, is_left: bool = False) -> str:

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
    def hash(self) -> str | None:
        """ Hash of root node. """
        if not self.__root: return

        return self.__root.value

    @property
    def root(self):
        return self.__root
    
    @property
    def size(self):
        return self.size