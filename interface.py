game = [['-'] * 7] * 7 


class FourGame():
    def __init__(self): #class constructor in python (there is no need to declare the attributes since the self.attribute do it for us)
        self.matrix = [['-']*7] * 7 #initialize an array of arrays who represents a matrix with 7 collums and 7 lines

    def __str__(self): #returns the string who graphicly represents the matrix of the game
        str = ""
        for line in self.matrix: #iterate through the collums
            for sign in line: #iterate through the lines
                str += sign
            str += "\n"
        return str
        

game = FourGame()
print(game)