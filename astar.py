from graph import Graph
from node import Node
from vector import Vector

class Astar():

    def __init__(self):
        self.graph = Graph()
        self.graph.setFirst(Node(0, Vector(0, 0)))
        for i in range(1, 7):
            self.graph.addInLineNext(Node(0, Vector(i, 0)), 0)

    def __heuristicCalculate(self):

    def __bestMove(self):
        bestNode = self.graph.first
        bestNode.setValue(self.__heuristicCalculate()) # falta o calculo da heuristica
        bestNodeHeuristic = bestNode.getValue()

        cur = self.graph.first.getNext()

        while (cur != None):
            cur.setValue(self.__heuristicCalculate()) # falta o calculo da heuristica
            value = cur.getValue()
            if symbol == 'O' and bestNodeHeuristic > value:
                bestNodeHeuristic = value
            elif symbol == 'X' and bestNodeHeuristic < value:
                bestNodeHeuristic = value

            cur = cur.getNext()
        
        return bestNode
        

    def play(self, x, y):
        
        cur = self.graph.first
        for _ in range(x):
            cur = cur.getNext()
        
        cur.setCoords(Vector(x, y+1))
        return self.__bestMove()
        	
Astar()
