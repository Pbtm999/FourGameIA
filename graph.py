from node import Node

class Graph():

    def __init__(self):
        self.first = None

    def setFirst(self, node):
        self.first = node

    def getFirst(self):
        return self.first
    
    def addNext(self, node):
        cur = self.first
        while cur.getNext() != None:
            cur = cur.getNext()

        cur.setNext(node)

    def addInLineNext(self, node, height):
        cur = self.first
        for _ in range (height):
            cur = cur.getNext()

        while cur.getInlineNext() != None:
            cur = cur.getInlineNext()
        
        cur.setInlineNext(node)