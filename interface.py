class FourGame():
    # params: self: Class FourGame instance | collums: integer number of collums for the game | lines: integer number of lines for the game
    def __init__(self, collums, lines): # class constructor in python (there is no need to declare the attributes since the self.attribute do it for us)
        self.matrix = [['-' for _ in range(collums)] for _ in range(lines)]
        self.collums = collums
        self.lines = lines
        self.plays = 0

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
        for i in range(self.lines-1, -1, -1):
            if self.matrix[i][collum] == '-':
                self.matrix[i][collum] = symbol
                return i
        return -1 # retuns in case the collum is full

    def __checkRepetions(self, length, line, collum, linei, collumi, symbol):
        count = 0
        for _ in range(length, 0, -1):
            if self.matrix[line][collum] == '-': 
                return False
            if self.matrix[line][collum] == symbol: 
                count += 1
            else: 
                count = 0
            collum += collumi 
            line += linei 
            
            if count == 4: return True



        return False

    def __checkWin(self, collum, line, symbol):
        return self.__checkRepetions(self.lines, self.lines-1, collum, -1, 0, symbol) or self.__checkRepetions(self.collums, line, 0, 0, 1, symbol) # first checks collums secound check the collums
    
    # params: self: Class FourGame instance | collum: integer number of collum to play | character symbol ('X', 'O')
    # return: string or false
    def makeMove(self, collum, symbol):
        self.plays += 1
        
        line = self.__insertSymbol(collum, symbol)
        if line == -1: return -1, '' # invalid move the collum is full

        # Evaluate Code (A* and MCTS)
        
        # Verify if it should end the game (in case of someone win or the board is full)
        if self.__checkWin(collum, line, symbol): 
            return 2, symbol
        elif (self.plays == self.collums*self.lines): 
            return 1, ''
        return 0, ''


game = FourGame(7, 6)
end = False
move = 'X'

while not end:
    col = int (input('Coluna: '))
    result, winner = game.makeMove(col, move)

    print(game)

    match result:
        case -1:
            end = True
            print("Invalid Move!")
            break
        case 0:
            print("Nice Move!")
        case 1:
            end = True
            print("It's a Draw!!")
        case 2:
            end = True
            print('The symbol ' + winner + ' just won!')
        
    if move == 'X': move = 'O'
    else: move = 'X'