from graph import Graph
from node import Node

class Astar():

    def __init__(self):
        self.graph = Graph()
        self.first = Node(1)
        self.addNext(Node(2))
        print(self.first.getNext().getValue())
