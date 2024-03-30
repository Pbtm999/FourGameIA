class Queue():

    def __init__(self):
        self.stack = []
        self.size = 0

    def isEmpty(self):
        if self.size ==0:
            return True
        return False

    def pop(self):
        if self.size != 0:
            self.size = self.size - 1
            return self.stack.pop(self.size)
        else:
            return None

    def top(self):
        if self.size != 0:
            return self.stack.pop(self.size-1)
        else:
            return None
        
    def add(self, value):
        self.stack.append(value)
        self.size = self.size + 1