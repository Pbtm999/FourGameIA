class FourGame():
    # params: self: Class FourGame instance | collums: integer number of collums for the game | lines: integer number of lines for the game
    def __init__(self, collums, lines): # class constructor in python (there is no need to declare the attributes since the self.attribute do it for us)
        self.matrix = [['-' for _ in range(collums)] for _ in range(lines)]
        self.collums = collums
        self.lines = lines

    # params: self: Class FourGame instance
    def __str__(self): # returns the string who graphicly represents the matrix of the game
        str = ""
        for line in self.matrix: # iterate through the collums
            for sign in line: # iterate through the lines
                str += sign
            str += "\n"
        return str

    # params: self: Class FourGame instance | collum: integer number of collum to play | character symbol ('X', 'O')
    def __insertSymbol(self, collum, symbol): # private method to insert a symbol into the array
        collum -= 1 # reduce one since the array starts at 0
        for i in range(self.lines-1, -1, -1):
            if self.matrix[i][collum] == '-':
                self.matrix[i][collum] = symbol
                break
    
    # params: self: Class FourGame instance | collum: integer number of collum to play | character symbol ('X', 'O')
    # return: boolean
    def play(self, collum, symbol):
        self.__insertSymbol(collum, symbol)
        # Evaluate Code (A* and MCTS)


game = FourGame(7, 6)
game.play(2, 'X')
game.play(2, 'X')
game.play(3, 'X')
game.play(4, 'O')
print(game)