class Node():

    def __init__(self):
        self.next = None
        self.inlineNext = None
    
    def setNext(self, next):
        self.next = next
    
    def setInlineNext(self, inlineNext):
        self.inlineNext = inlineNext

    def getNext(self):
        return self.next
    
    def getInlineNext(self):
        return self.inlineNext


