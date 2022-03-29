"""
CS3C, Assignment #8, Graphs
Gabriel Alon
Vertex Class
"""


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedto = {}

    def addNeighbor(self, nbr, cost=None):
        self.connectedto[nbr] = cost

    def getConnections(self):
        return self.connectedto.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedto[nbr]


"""
class Vertex:
    def __init(self,id,):
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
####
class Vertex:
    def __init(self,id, out_edges = None):
        self.id = id
        out_edges = []

    def add_edge(self,id, cost):
        new_edge = Edge(id,self,cost)
        self.out_edges.append(edge)
        return edge

    def __str__(self):
        return f"{self.__class__.__name__}=({self.id},{self.out_edges}"

    def __repr(self):
        return str(self)
ok = Node(None)
ok = Stack(None)
"""

# min 3:55 in general graph implmentaiton
# https://www.youtube.com/watch?v=_zQ-ju1Yoxk&list=PLJho_CCE0e85uly2IpbP0TZKT6FWdvoL_&index=83

# adjacency list
# efficient for sparse graph
# a: (b,3) (c,6) #means a points to b and c with these weights
# b: intentionally empty #only recieves from others
# c: (b:7)  #means c passes weight 7 to b
# from Assignment3.gabrielalonnode import *
# from Assignment3.gabrielalonstack import *
