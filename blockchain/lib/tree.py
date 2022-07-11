from dataclasses import InitVar, dataclass, field
import re
from .node import Node, Leaf
from .utils import hash

L_BRACKET_SHORT = '└─'
L_BRACKET_LONG = '└──'
T_BRACKET = '├──'
VERTICAL_BAR = '│'

@dataclass
class MerkleTree:
    """ Data Structure holding hashed data. """

    values: InitVar[list[str] | None] = None

    __root: Node | None = field(init=False, repr=True, default=None)

    def __post_init__(self, values: list[str] | None) -> None:
        """ Build the tree from list of values. """

        if not values: return
        
        leaves: list[Leaf] = [Leaf(value) for value in values]
        self.__root = self.__build_tree_recursive(leaves)

    @property
    def hash(self) -> str | None:
        """ Hash of root node. """
        if not self.__root: return

        return self.__root.value

    @property
    def root(self):
        """ Root (base) node of the tree. """
        return self.__root
    
    @property
    def depth(self) -> int:
        """ Height of the tree. """
        return self.__depth_recursive(self.__root)

    @property
    def size(self) -> int:
        """ Size of the tree. """
        if not self.__root: return 0
        
        return 1 + self.__root.left_count + self.__root.right_count

    @property
    def nb_leaves(self) -> int:
        """ Number of leaves. """
        return self.__number_leaves_recursive(self.__root)

    def __str__(self) -> str | None:
        """ Pretty print of tree. """

        if not self.__root: return

        return self.__to_string_recursive(self.__root)
    
    def __depth_recursive(self, node: Node | None) -> int:
        """ Recursively compute the size of a tree. """
        if node is None:
            return 0
        if node.parent is not None:
            return 1
        return 1 + max(self.__depth_recursive(node.left), self.__depth_recursive(node.right))
    
    def __number_leaves_recursive(self, node: Node | None) -> int:
        """ Recursicvely compute the number of leaves. """
        if node is None:
            return 0

        if node.is_leaf:
            return 1

        return self.__number_leaves_recursive(node.left) + self.__number_leaves_recursive(node.right)

    def __build_tree_recursive(self, nodes: list[Leaf]) -> Node:
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

    def __update_hash_ancestors(self, node: Node | None) -> None:
        """ Given a node, update the hash from leaf to root. """
        curr = node
        while curr:
            curr.compute_hash()
            curr = curr.parent

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
            self.__update_hash_ancestors(parent)
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