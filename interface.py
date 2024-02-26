class FourGame():
    # Parameters | self: Class FourGame instance | columns: Integer number of columns for the game | lines: Integer number of lines for the game
    def __init__(self, columns, lines):  # Class constructor (there is no need to declare the attributes since the self.attribute does it for us)
        self.matrix = [['-' for _ in range(columns)] for _ in range(lines)]
        self.columns = columns
        self.lines = lines
        self.plays = 0


    # Parameters | self: Class FourGame instance
    def __str__(self):  # Returns the string who graphically represents the matrix of the game
        str = ""
        for line in self.matrix:  # Iterate through the columns
            for sign in line:  # Iterate through the lines
                str += sign
            str += "\n"
        return str


    # Parameters | self: Class FourGame instance | column: Integer number of column to play | Character symbol ('X', 'O')
    def __insertSymbol(self, column, symbol):  # Private method to insert a symbol into the array
        for i in range(self.lines-1, -1, -1):
            if self.matrix[i][column] == '-':
                self.matrix[i][column] = symbol
                return i
        return -1  # Returns in case the column is full
    

    def __checkWinDiagonal1(self, lines,columns, symbol):
        for x in range(lines - 3):
            for y in range(3, columns):
                if (self.matrix[x][y] == symbol and self.matrix[x+1][y+1]==symbol and self.matrix[x+2][y+2]==symbol and self.matrix[x+3][y+3]==symbol):
                    return True
                

    def __checkWinDiagonal2(self, lines,columns, symbol):
        for x in range(lines - 3):
            for y in range(3, columns):
                if (self.matrix[x][y] == symbol and self.matrix[x+1][y-1]==symbol and self.matrix[x+2][y-2]==symbol and self.matrix[x+3][y-3]==symbol):
                    return True



    def __checkRepetitions(self, length, line, column, lineCount, columnCount, symbol):
        count = 0
        for _ in range(length, 0, -1):
            if self.matrix[line][column] == '-': 
                return False
            if self.matrix[line][column] == symbol: 
                count += 1
            else: 
                count = 0
            column += columnCount
            line += lineCount
            
            if count == 4: return True

        return False
    

    def __checkWin(self, column, line, symbol):
        # Check for win horizontally
        if self.__checkRepetitions(self.columns, line, 0, 0, 1, symbol):
            return True
        
        # Check for win vertically
        if self.__checkRepetitions(self.lines, self.lines-1, column, -1, 0, symbol):
            return True

        # Check for win diagonally
        if self.__checkWinDiagonal1(self.lines, self.columns, symbol):
            return True
        if self.__checkWinDiagonal2(self.lines, self.columns, symbol):
            return True
        

        """
        bottom left para top right

        if self.__checkDiagonalWin(self,line, column, symbol):
            return True
        """
        return False
    
                
   # def __checkWinDiagonal2(self, lines, columns, symbol):
        
        


    # Parameters | self: Class FourGame instance | column: Integer number of column to play | Character symbol ('X', 'O')
    # Return: string or false
    def makeMove(self, column, symbol):
        self.plays += 1
        
        line = self.__insertSymbol(column - 1, symbol)
        if line == -1: return -1, ''  # Invalid move, the column is full

        # Evaluate Code (A* and MCTS)
        
        # Verify if it should end the game (in case if someone wins or the board is full)
        if self.__checkWin(column - 1, line, symbol): 
            return 2, symbol
        
        elif (self.plays == self.columns*self.lines): 
            return 1, ''
        return 0, ''


def main():
    game = FourGame(7, 6)  # Creates a new game instance
    end = False  # Initialize end to False to indicate that the game is not finished
    move = 'X'  # Initialize the first move as 'X'

    while not end:
        while True:  # Loop to handle input until a valid move is made
            try:
                col = int(input('Column: '))
                if col < 1 or col > 7:
                    raise ValueError  # Raise a ValueError if the input isn't in the range 1-7
                break
            except ValueError:
                print("Invalid Input! Please enter a number from 1 to 7.")

        result, winner = game.makeMove(col, move)  # Make a move in a certain column

        print(game)  # Print the current state of the game board

        match result:
            case -1:  # Case when a column is full
                print("Invalid Move! Please choose another column.")
            case 0:  # Case for when a valid move is done
                print("Nice Move!")
            case 1:  # Case for a draw
                end = True
                print("It's a Draw!!")
            case 2:  # Case for a win
                end = True
                print('The symbol ' + winner + ' just won!')

        if move == 'X':
            move = 'O'
        else:
            move = 'X'


if __name__ == '__main__':
    main()