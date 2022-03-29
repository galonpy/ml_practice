"""
CS3C, Assignment #3, Linked Lists and Stacks
Gabriel Alon
Stack Class implemented as a linked list
"""
from Assignment3.gabrielalonnode import Node


class Stack:
    """
    Implement a stack by using Linked lists.
    """

    def __init__(self, data=None):
        #   stack = self.create_stack(data)
        self.head = None
        if data:
            self.push(data)

    def push(self, data):
        """
        new node is added as head, and its next is the previous head
        """
        # recieves data or a node object?
        if self.head is not None:
            temp = Node(data)
            temp.next = self.head
            self.head = temp
        # self.head.next = temp
        # self.head = temp
        else:
            self.head = Node(data)

    def pop(self):
        popped = self.head
        self.head = self.head.next  # one before the top is now self.head -- Its next is intact as Node attrbiute
        popped.next = None  # is this modidying the same object instance as intended?
        return popped.data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

    def is_empty(self):
        return self.head == None

    @classmethod
    def create_stack(cls):
        """ Creates stack """
        return Stack()

    def delete_stack(self):
        """

        while self.head.next != None:
            next_node = self.head.next
            self.head.data = None
            self.head = next_node
        self.head.data = None
        """
        while self.head != None:
            temp = self.head
            self.head.next = self.head
            temp = None
