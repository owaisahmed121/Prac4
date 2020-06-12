""" Stack ADT and an array implementation.

Defines a generic abstract stack with the usual methods, and implements 
a stack using arrays. Also defines UnitTests for the class.
"""


import unittest
from abc import ABC, abstractmethod 
from enum import Enum
from typing import TypeVar, Generic

T = TypeVar('T')


class Stack(ABC, Generic[T]):
    def __init__(self) -> None:
        self.length = 0

    @abstractmethod
    def push(self, item: T) -> None:
        """ Pushes an element to the top of the stack."""
        pass

    @abstractmethod
    def pop(self) -> T:
        """ Pops an element from the top of the stack."""
        pass

    @abstractmethod
    def peek(self) -> T:
        """ Pops the element at the top of the stack."""
        pass

    def __len__(self) -> int:
        """ Returns the number of elements in the stack."""
        return self.length

    def is_empty(self) -> bool:
        """ True if the stack is empty. """
        return len(self) == 0

    @abstractmethod
    def is_full(self) -> bool:
        """ True if the stack is full and no element can be pushed. """
        pass

    def clear(self):
        """ Clears all elements from the stack. """
        self.length = 0


class Node(Generic[T]):
    """ Implementation of a generic Node class

    Attributes:
         item (T): the data to be stored by the node
         link (Node[T]): pointer to the next node

    ArrayR cannot create empty arrays. So MIN_CAPCITY used to avoid this.
    """

    def __init__(self, item: T = None) -> None:
        self.item = item
        self.link = None


class LinkStack(Stack[T]):
    """ Implementation of a stack with linked nodes.

    Attributes:
         length (int): number of elements in the stack (inherited)
    """

    def __init__(self) -> None:
        Stack.__init__(self)
        self.top = None

    def clear(self) -> None:
        """" Resets the stack
        :complexity: O(1)
        """
        super().clear()
        self.top = None

    def is_empty(self) -> bool:
        """ Returns whether the stack is empty
        :complexity: O(1)
        """
        return self.top is None

    def is_full(self) -> bool:
        """ Returns whether the stack is full
        :complexity: O(1)
        """
        return False

    def push(self, item: T) -> None:
        """ Pushes an element to the top of the stack.
        :complexity: O(1)
        """
        new_node = Node(item)
        new_node.link = self.top
        self.top = new_node
        self.length += 1

    def pop(self) -> T:
        """ Pops the element at the top of the stack.
        :pre: stack is not empty
        :complexity: O(1)
        :raises Exception: if the stack is empty
        """
        if self.is_empty():
            raise Exception("Stack is empty")

        item = self.top.item
        self.top = self.top.link
        self.length -= 1
        return item

    def peek(self) -> T:
        """ Returns the element at the top, without popping it from stack.
        :pre: stack is not empty
        :complexity: O(1)
        :raises Exception: if the stack is empty
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.item
