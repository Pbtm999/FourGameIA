class Node():

    def __init__(self, value):
        self.value = value
        self.next = None
        self.inlineNext = None
    
    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def setNext(self, next):
        self.next = next
    
    def setInlineNext(self, inlineNext):
        self.inlineNext = inlineNext

    def getNext(self):
        return self.next
    
    def getInlineNext(self):
        return self.inlineNext


