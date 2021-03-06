from dataclasses import InitVar, dataclass, field
from enum import Enum, auto
import re
from .node import Node, Leaf
from .utils import digest

L_BRACKET_SHORT = '└─'
L_BRACKET_LONG = '└──'
T_BRACKET = '├──'
VERTICAL_BAR = '│'

class POSITION(Enum):
    RIGHT = auto()
    LEFT = auto()

@dataclass
class MerkleTree:
    """ Data Structure holding hashed data. """

    values: InitVar[list[str] | None] = None

    __root: Node | None = field(init=False, repr=True, default=None)

    def __post_init__(self, values: list[str] | None) -> None:
        """ Build the tree from list of values. """

        if not values: 
            self.__root = None
            return
        
        leaves = [Leaf(digest(value)) for value in values]
        for leaf in leaves:
            self.insert(leaf)

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
    
    def __depth_recursive(self, node: Node | None) -> int:
        """ Recursively compute the size of a tree. """
        if node is None:
            return 0
        if node.parent is not None:
            return 1
        return 1 + max(self.__depth_recursive(node.left), self.__depth_recursive(node.right))

    @property
    def size(self) -> int:
        """ Size of the tree. """
        if not self.__root: return 0
        
        return 1 + self.__root.left_count + self.__root.right_count

    @property
    def nb_leaves(self) -> int:
        """ Number of leaves. """
        return self.__number_leaves_recursive(self.__root)
    
    def __number_leaves_recursive(self, node: Node | None) -> int:
        """ Recursicvely compute the number of leaves. """
        if node is None:
            return 0

        if node.is_leaf:
            return 1

        return self.__number_leaves_recursive(node.left) + self.__number_leaves_recursive(node.right)

    def insert(self, leaf: Leaf) -> None:
        """ Insertion of a new Leaf in the tree"""

        # Find the last in order Leaf
        last_leaf = self.get_inorder_leaf()

        if not last_leaf:
            self.__root = leaf
            return

        # Keep the position before uprooting the leaf of its ancestor's branch
        position = POSITION.LEFT if (last_leaf.is_left_child or last_leaf.parent is None) else POSITION.RIGHT
        fork_node = last_leaf.parent

        # Create the new branch and attach the leaves (the one uprooted and the one inserted)
        subroot = Node(digest(last_leaf.value + leaf.value), last_leaf, leaf, fork_node)

        if not fork_node:
            self.__root = subroot
            return

        if position == POSITION.LEFT:
            fork_node.left = subroot
        if position == POSITION.RIGHT:
            fork_node.right = subroot

        # Update the hashes of the ancestors bottom-up
        curr = fork_node
        while curr:
            curr.digest_hashes()
            curr = curr.parent
    
    def insert_old(self, leaf: Leaf) -> None:
        """ 
        DEPRECATED: PLEASE USE REGULAR INSERT.
        Add a node to the tree. In order insertion. 
        Plus not working: no update of nodes.
        """

        if not self.__root:
            self.__root = leaf
            return

        if self.__root.is_leaf:
            left = self.__root
            self.__root = Node(digest(left.value + leaf.value), left, leaf, None)

        else:
            last_leaf = self.get_inorder_leaf()
            if last_leaf:
                subroot = last_leaf.parent
                left = Leaf(last_leaf.value)
                right = leaf
                intermediary = Node(digest(left.value + right.value), left, right, subroot)
                
                if last_leaf.is_left_child:
                    subroot.left = intermediary #type: ignore
                elif last_leaf.is_right_child:
                    subroot.right = intermediary #type: ignore
                left.parent = intermediary
                right.parent = intermediary
    
    def get_inorder_leaf(self) -> Leaf | None:
        """ Get the node whoch should receive the leaf. """
        if self.__root is None:
            return self.__root

        return self.__inorder_leaf_recursive(self.__root)

    def __inorder_leaf_recursive(self, node: Node | None, parent: Node | None = None) -> Leaf | None:
        """ Recursive insertion in order (left first). """

        if node is None:
            return parent # type: ignore
        
        if (node.right_count == node.left_count):
            return self.__inorder_leaf_recursive(node.left, node)
        
        elif (node.right_count < node.left_count):

            if (node.left_count % 2 == 1):
                return self.__inorder_leaf_recursive(node.right, node)
            else:
                return self.__inorder_leaf_recursive(node.left, node)

    def find_value(self, value: str) -> None:
        """ Find a node and returns it's position. """
        raise NotImplementedError()

    def find_hash(self, hash: str) -> None:
        raise NotImplementedError()

    def __str__(self) -> str:
        """ Pretty printter of tree. """

        if not self.__root: return f'\n{L_BRACKET_LONG} None'

        return self.__to_string_recursive(self.__root)

    def __to_string_recursive(self, node: Node, depth: int = 0, indent: int = 3, ignored: list = []) -> str:

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

        if node.is_left_child:
            out += f' {T_BRACKET}'
        if node.is_right_child:
            out += f' {L_BRACKET_LONG}'
            ignored.append(depth)
        
        out += f"{node.value} ({node.position})\n "

        args = (depth + 1, indent, ignored.copy())

        if node.left:
            out += self.__to_string_recursive(node.left, *args)
        if node.right:
            out += self.__to_string_recursive(node.right, *args)

        return out