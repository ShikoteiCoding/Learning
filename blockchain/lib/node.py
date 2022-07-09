from __future__ import annotations

from dataclasses import dataclass, field

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

    @property
    def right(self) -> Node | None:
        """ The right child of the node. """
        return self.__right

    @property
    def left(self) -> Node | None:
        """ The left chiled of the node. """
        return self.__left

    @property
    def parent(self) -> Node | None:
        """ The parent node. """
        return self.__parent