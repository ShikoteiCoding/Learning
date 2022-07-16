from __future__ import annotations

from dataclasses import dataclass, field
from .utils import digest_double_entries


@dataclass(slots=True)
class Node:
    """ Node sub-element of Markle Tree """
    __value: str = field(init=True, repr=True)
    __left: Node | None = field(init=True, repr=False, default=None)
    # Right can be None if single child Node. Left can never be None in a Node.
    __right: Node | None = field(init=True, repr=False, default=None)
    # Parent can be none and set later.
    __parent: Node | None = field(init=True, repr=False, default=None)

    def __post_init__(self):
        # Deal with parent linkage at the instanciation.
        if self.__left:
            self.__left.parent = self
        if self.__right:
            self.__right.parent = self

    @property
    def value(self) -> str:
        """ The hash stored by the node. """
        return self.__value

    @value.setter
    def value(self, val: str) -> None:
        """ Set the hash stored in the node. """
        self.__value = val

    @property
    def left(self) -> Node | None:
        """ The left child of the node. """
        return self.__left

    @left.setter
    def left(self, node: Node | None) -> None:
        """ Set the left child of the node. """
        self.__left = node

    @property
    def right(self) -> Node | None:
        """ The right child of the node. """
        return self.__right

    @right.setter
    def right(self, node: Node | None) -> None:
        """ Set the left child of the node. """
        self.__right = node

    @property
    def parent(self) -> Node | None:
        """ The parent node. """
        return self.__parent
    
    @parent.setter
    def parent(self, node: Node | None) -> None:
        """ Set the parent node. """
        self.__parent = node

    @property
    def left_count(self) -> int:
        """ The number of left descendant nodes. """
        return self.__count_recursive(self.left)

    @property
    def right_count(self) -> int:
        """ The number of right descendant nodes. """
        if not self.right: return 0
        return self.__count_recursive(self.right)

    @property
    def is_leaf(self) -> bool:
        """ Return False for a Node. """
        return isinstance(self, Leaf)

    @property
    def is_left_child(self) -> bool:
        """ Return if is left child of parent Node. """
        if self.parent:
            return self == self.parent.left
        return False

    @property
    def is_right_child(self) -> bool:
        """ Return if is left child of parent Node. """
        if self.parent:
            return self == self.parent.right
        return False

    @property
    def position(self) -> str:
        if self.is_left_child: return 'left'
        elif self.is_right_child: return 'right'
        else: return 'no parent'

    def __eq__(self, other: Node) -> bool:
        """ Return True if the hash is the same. """
        return self.__value == other.__value

    def __count_recursive(self, node: Node | None) -> int:
        """ Compute the number of child in the node provided. """
        if node is None:
            return 0

        return 1 + self.__count_recursive(node.left) + self.__count_recursive(node.right)

    def digest_hashes(self) -> None:
        """ 
        Digest the hash from the left and right nodes / leaves. 
        Double left value if no right value.
        """
        if not self.__left: raise Exception("Node is a Leaf. Can't compute hash from non-existent children.")
        left_value = self.__left.__value
        right_value = self.__right.__value if self.__right else self.__left.__value
        self.__value = digest_double_entries(left_value, right_value)

@dataclass(slots=True)
class Leaf(Node):
    """ Leaf of a Tree. Node without children. Used to browse the tree  more efficiently. """