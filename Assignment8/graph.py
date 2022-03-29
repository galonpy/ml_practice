"""
CS3C, Assignment #8, Graphs
Gabriel Alon
Graph Class
"""
from Assignment8.vertex import *


class Graph:
    def __init__(self):
        self.vertices = {}  # key id string of a point, value is vertex object
        # shouldnt self.vertices be an ordered list so i can infer the value with a fixed index

    def addVertex(self, key):
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex

    def getGraph(self):
        try:
            result = []
            for key in self.vertices:
                results = self.vertices[key].getConnections()
                for i in results:
                    result.append(
                        (f"from {self.vertices[key].id} to {i.id} of weight {self.vertices[key].getWeight(i)}"))
            return (result)
        except:
            pass

    def addEdge(self, node_1, node_2, weight):
        self.vertices[node_1].addNeighbor(self.vertices[node_2], weight)


G = Graph()
G.addVertex('a')
G.addVertex('b')
G.addVertex('c')
G.addVertex('d')
G.addVertex('e')

G.addEdge('a', 'b', 4)
G.addEdge('a', 'c', 1)
G.addEdge('c', 'b', 2)
G.addEdge('b', 'e', 4)
G.addEdge('c', 'd', 4)

print(G.getGraph())

"""
['from a to b of weight 4', 'from a to c of weight 1', 'from b to e of weight 4',
 'from c to b of weight 2', 'from c to d of weight 4']
"""