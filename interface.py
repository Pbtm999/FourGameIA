from astar import Astar
from miniMax import MinMax
from mcts import MCTS

class FourGame():
    # Parameters | self: Class FourGame instance | columns: Integer number of columns for the game | lines: Integer number of lines for the game
    def __init__(self, columns, lines):  # Class constructor (there is no need to declare the attributes since the self.attribute does it for us)
        self.matrix = [['-' for _ in range(columns)] for _ in range(lines)]
        self.columns = columns
        self.lines = lines
        self.plays = 0
        self.toPlay = 'O'
        self.result = None


    # Parameters | self: Class FourGame instance
    def __str__(self):  # Returns the string who graphically represents the matrix of the game
        str = "=============================\n"
        for line in self.matrix:  # Iterate through the columns
            for sign in line:  # Iterate through the lines
                str += '| ' + sign + ' '
            str += "|\n"
        str += "=============================\n"
        str += "  1   2   3   4   5   6   7  \n"
        return str


    # Parameters | self: Class FourGame instance | column: Integer number of column to play | Character symbol ('X', 'O')
    def __insertSymbol(self, column, symbol):  # Private method to insert a symbol into the array
        for i in range(self.lines-1, -1, -1):
            if self.matrix[i][column] == '-':
                self.matrix[i][column] = symbol
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

            while lineI <= 5 and lineI >= 0 and columnI <= 6 and column >= 0 and self.matrix[lineI][columnI] == symbol:
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

    def getMatrix(self):
        return self.matrix

    def gameOver(self):
        return self.result is not None or self.plays == self.columns * self.lines
    
    def getLegalMoves(self):
        legalMoves = []
        for i in range(7):
            if self.matrix[5][i] == '-':
                legalMoves.append(i)

        return legalMoves


def main():
    game = FourGame(7, 6)  # Creates a new game instance
    end = False  # Initialize end to False to indicate that the game is not finished

    move = input('Escolhe o símbolo com que queres jogar (X ou O): ')

    try:
        if move != 'X' and move != 'O':
            raise ValueError
    except ValueError:
        print('O símbolo deve ser X ou O')
        return
    
    match move:
        case 'X':
            iaSymbol = 'O'
        case 'O': 
            iaSymbol = 'X'

    print('===============\n| 1 -> A*     |\n| 2 -> MTC    |\n| 3 -> MinMax |\n===============')
    algoResp = int(input('Escolhe contra que algoritmo gostarias de jogar: '))
    match algoResp:
        case 1:
            algo = Astar(iaSymbol)
        case 2:
            algo = MCTS(game)
        case 3:
            algo = MinMax(iaSymbol, move)

    while not end:
        invalid = False
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
                invalid = True
                print("Invalid Move! Please choose another column.")
            case 0:  # Case for when a valid move is done
                print("Nice Move!")
            case 1:  # Case for a draw
                end = True
                print("It's a Draw!!")
            case 2:  # Case for a win
                end = True
                print('The symbol ' + winner + ' just won!')
        
        if not end and not invalid:
            result, winner = game.makeMove(algo.play(game.getMatrix())+1, iaSymbol)  # Make a move in a certain column

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
        
if __name__ == '__main__':
    main()