from typing import TypeVar, Generic
from list import SortedLinkList
K = TypeVar('K')
I = TypeVar('I')


class BinarySearchListTreeNode(Generic[K, I]):
    """ Implementation of a BST List Node

    Attributes:
         key (K): the key to be stored in the node
         items (SortedLinkList[I]): the sorted list of items in the node
         left (BinarySearchListTreeNode[K, I]): pointer to left child
         right (BinarySearchListTreeNode[K, I]): pointer to right child
    """

    def __init__(self, key: K, item: I = None) -> None:
        self.key = key
        self.items = SortedLinkList()
        self.items.append(item)
        self.left = None
        self.right = None

    def __str__(self):
        """Key and associated data items"""
        return " (" + str(self.key) + ", " + str(self.items) + " ) "


class BinarySearchListTree(Generic[K, I]):
    """ Implementation of a BST using a sorted list for the item.

    Attributes:
         root (BinarySearchListTreeNode): reference to the root of the BST
    """
    def __init__(self) -> None:
        self.root = None

    def __getitem__(self, key: K) -> SortedLinkList[I]:
        raise NotImplementedError

    def __setitem__(self, key: K, item: I) -> None:
        raise NotImplementedError
