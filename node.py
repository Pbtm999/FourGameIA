class Node():

    def __init__(self, value, vector):
        self.value = value
        self.coords = vector
        self.next = None
        self.inlineNext = None
    
    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def setCoords(self, vector):
        self.coords = vector

    def getCoords(self):
        return self.coords

    def setNext(self, next):
        self.next = next
    
    def setInlineNext(self, inlineNext):
        self.inlineNext = inlineNext

    def getNext(self):
        return self.next
    
    def getInlineNext(self):
        return self.inlineNext


