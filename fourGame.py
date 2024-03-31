class FourGame():
    # Parameters | self: Class FourGame instance | columns: Integer number of columns for the game | lines: Integer number of lines for the game
    def __init__(self, columns, lines):  # Class constructor (there is no need to declare the attributes since the self.attribute does it for us)
        self.state = [['-' for _ in range(columns)] for _ in range(lines)]
        self.columns = columns
        self.lines = lines
        self.plays = 0
        self.toPlay = 'O'
        self.result = None


    # Parameters | self: Class FourGame instance
    def __str__(self):  # Returns the string who graphically represents the matrix of the game
        str = "=============================\n"
        for line in self.state:  # Iterate through the columns
            for sign in line:  # Iterate through the lines
                str += '| ' + sign + ' '
            str += "|\n"
        str += "=============================\n"
        str += "  1   2   3   4   5   6   7  \n"
        return str


    # Parameters | self: Class FourGame instance | column: Integer number of column to play | Character symbol ('X', 'O')
    def __insertSymbol(self, column, symbol):  # Private method to insert a symbol into the array
        for i in range(self.lines-1, -1, -1):
            if self.state[i][column] == '-':
                self.state[i][column] = symbol
                if symbol == 'X':
                    self.toPlay = 'O'
                else:
                    self.toPlay = 'X'
                return i
        return -1  # Returns in case the column is full

    def __checkRepetitions(self, line, column, lineCount, columnCount, symbol):
        count = 0
        lineI = line
        columnI = column
        for _ in range(2):

            while lineI <= 5 and lineI >= 0 and columnI <= 6 and columnI >= 0 and self.state[lineI][columnI] == symbol:
                count += 1
                columnI += columnCount
                lineI += lineCount
                if count == 4: 
                    self.result = symbol
                    return True
 
            columnCount *= -1
            lineCount *= -1
            columnI = column + columnCount
            lineI = line + lineCount

        return False
    
    def __checkWin(self, column, line, symbol):

        # Check for win vertically
        if self.__checkRepetitions(line, column, -1, 0, symbol):
            return True
            
        # Check for win horizontallys
        if self.__checkRepetitions(line, column, 0, 1, symbol):
            return True
        
        # Check for win main diagonal
        if self.__checkRepetitions(line, column, -1, 1, symbol):
            return True

        # Check for win inverse diagonal
        if self.__checkRepetitions(line, column, 1, 1, symbol):
            return True
        
        return False
        
    
    # Parameters | self: Class FourGame instance | column: Integer number of column to play | Character symbol ('X', 'O')
    # Return: string or false
    def makeMove(self, column, symbol):
        
        line = self.__insertSymbol(column - 1, symbol)
        if line == -1: return -1, ''  # Invalid move, the column is full

        self.plays += 1
        
        # Verify if it should end the game (in case if someone wins or the board is full)
        if self.__checkWin(column - 1, line, symbol): 
            return 2, symbol
        elif (self.plays == self.columns*self.lines): 
            return 1, ''
        return 0, ''

    def gameOver(self):
        return self.result is not None or self.plays == self.columns * self.lines
    
    def gameDraw(self):
        return self.plays == self.columns * self.lines
    
    def getLegalMoves(self):
        legalMoves = []
        for i in range(7):
            if self.state[0][i] == '-':
                legalMoves.append(i)

        return legalMoves