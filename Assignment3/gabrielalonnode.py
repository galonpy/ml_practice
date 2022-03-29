"""
CS3C, Assignment #3, Linked Lists and Stacks
Gabriel Alon
Node Class as a basis for a linked list
"""


class Node:
    def __init__(self, init):
        self._data = init
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        if data == None:
            self._data = data
        elif self.helper_node(data) and helper_value(data) and helper_printable(data):
            self._data = data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self._next = node

    def helper_value(self, the_str):
        # value is legit ({[ ]})
        try:
            for achar in the_str:
                if the_str in '({[]})':
                    return True
                else:
                    return False
        except:
            return False

    def helper_printable(self, the_str):
        for achar in the_str:
            if (achar.isprintable()):
                pass
            else:
                return False
        return True

    def helper_node(self, the_str):
        if the_str.next is None:
            return True
        else:
            return False
        # check if node already points to another node
        # forbidden if breaks linkedin list sequential aspect?
