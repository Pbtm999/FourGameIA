game = [['-'] * 7] * 7 


class FourGame():
    def __init__(self):
        self.matrix = [['-']*7] * 7 #initialize an array with 7 collums and 7 lines

    def __str__(self):    
        str = ""
        for line in self.matrix: #iterate through the collums
            for sign in line: #iterate through the lines
                str += sign
            str += "\n"
        return str
        

game = FourGame()
print(game)