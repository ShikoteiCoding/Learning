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
    """ Data Structure holding hashed data. """

    values: InitVar[list[str] | None] = None

    __root: Node | None = field(init=False, repr=True, default=None)
    __size: int = field(init=False, repr=True, default=0)
    __depth: int = field(init=False, repr=True, default=0)

    def __post_init__(self, values: list[str] | None) -> None:
        """ Build the tree from list of values. """

        if not values: return
        
        nodes: list[Node] = [Node(hash(value)) for value in values]
        self.__root = self.__build_tree_recursive(nodes)

    def __build_tree_recursive(self, nodes: list[Node]) -> Node:
        """ Recursively build the nodes and their descendants. """

        pivot: int = len(nodes) // 2

        if len(nodes) == 2:
            return Node(hash(nodes[0].value + nodes[1].value), nodes[0], nodes[1])
        if len(nodes) == 1:
            return Node(hash(nodes[0].value), nodes[0])

        left: Node = self.__build_tree_recursive(nodes[pivot:])
        right: Node = self.__build_tree_recursive(nodes[:pivot])
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
        
        out += f"{node.value} ({'right' if is_right == True else 'left'})\n "

        args = (depth + 1, indent, ignored.copy())

        if node.left:
            out += self.__to_string_recursive(node.left, *args, is_left=True)
        if node.right:
            out += self.__to_string_recursive(node.right, *args, is_right=True)

        return out

    def insert(self, value: str) -> None:
        """ Add a node to the tree. In order insertion (not a BST, just a BT). """

        if not self.__root: 
            self.__root = Node(hash(value))
        else:
            self.__insert_recursive(self.__root, value, None)

    def __insert_recursive(self, node: Node | None, value: str, parent: Node | None) -> Node:
        """ Recursive insertion in order (left first). """

        if node is None:
            node = Node(hash(value), None, None, parent)
            return node
        
        if (node.right_count == node.left_count):
            node.left = self.__insert_recursive(node.left, value, node)
        
        elif (node.right_count < node.left_count):

            if (node.left_count % 2 == 1):
                node.right = self.__insert_recursive(node.right, value, node)
            else:
                node.left = self.__insert_recursive(node.left, value, node)
    
        return node

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