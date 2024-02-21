game = [['-'] * 7] * 7 #initialize an array with 7 collums and 7 lines

def drawInterface(game):
    str = ""
    for line in game: #iterate through the collums
        for sign in line: #iterate through the lines
            str += sign
        print(str)
        str = ""

drawInterface(game)