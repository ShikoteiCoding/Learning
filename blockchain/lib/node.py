from __future__ import annotations

from dataclasses import dataclass, field
from .utils import hash_entries

@dataclass(slots=True)
class Node:
    """ Node sub-element of Markle Tree """
    __value: str = field(init=True, repr=True, default="")
    __left: Node | None = field(init=True, repr=False, default=None)
    __right: Node | None = field(init=True, repr=False, default=None)
    __parent: Node | None = field(init=True, repr=False, default=None)

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
    def left(self, node: Node) -> None:
        """ Set the left child of the node. """
        self.__left = node

    @property
    def right(self) -> Node | None:
        """ The right child of the node. """
        return self.__right

    @right.setter
    def right(self, node: Node) -> None:
        """ Set the left child of the node. """
        self.__right = node

    @property
    def parent(self) -> Node | None:
        """ The parent node. """
        return self.__parent
    
    @parent.setter
    def parent(self, node: Node) -> None:
        """ Set the parent node. """
        self.__parent = node

    @property
    def left_count(self) -> int:
        """ The number of left descendant nodes. """
        if not self.left: return 0
        return self.__count_recursive(self.left)

    @property
    def right_count(self) -> int:
        """ The number of right descendant nodes. """
        if not self.right: return 0
        return self.__count_recursive(self.right)

    @property
    def is_leaf(self) -> bool:
        """ Return true if is a leaf in the tree. """
        return (self.left is None and self.right is None)

    def __eq__(self, other: Node) -> bool:
        """ Return True if the hash is the same. """
        return self.__value == other.value

    def __count_recursive(self, node: Node | None) -> int:
        """ Compute the number of child in the node provided. """
        if node is None:
            return 0

        return 1 + self.__count_recursive(node.left) + self.__count_recursive(node.right)

    def update_hash(self) -> None:
        """ """
        left_value = self.left.value if self.left else ''
        right_value = self.right.value if self.right else ''
        self.value = hash_entries(left_value, right_value)