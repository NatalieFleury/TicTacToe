
board = []
for x in range(2):
    board.append([ ' ', '|', ' ', '|', ' ' ])
    board.append([ '-', '-', '-', '-', '-' ])
board.append([ ' ', '|', ' ', '|', ' ' ])

def printBoard():
    print()
    for x in board:
        print("".join(x))
    print()

printBoard()
print("Let's get started!")

global currSymbol

def switchSymbol(char):
    if char == 'X':
        return 'O'
    return 'X'

def gameOver():
    for x in range(3):
        if ((board[x*2][0] == 'X' or board[x*2][0] == 'O') and board[x*2][0] == board[x*2][2] and board[x*2][0] == board[x*2][4]) or ((board[0][x*2] == 'X' or board[0][x*2] == 'O') and board[0][x*2] == board[2][x*2] and board[0][x*2] == board[4][x*2]):
            return True
    if ((board[0][0] == 'X' or board[0][0] == 'O') and board[0][0] == board[2][2] and board[0][0] == board[4][4]) or ((board[4][0] == 'X' or board[4][0] == 'O') and board[4][0] == board[2][2] and board[4][0] == board[0][4]):
        return True
    return False

def main():
    currSymbol = 'X'
    while (not gameOver()):
        print("Player " + currSymbol + "\'s turn!")
        guessRow = int(input("Guess Row:"))
        guessCol = int(input("Guess Column:"))
        if guessRow > 2 or guessRow < 0 or guessCol > 2 or guessCol < 0:
            print("Out of range, dummy!")
        elif board[guessRow*2][guessCol*2] != ' ':
            print("That spot is taken, dummy!")
        else:
            board[guessRow*2][guessCol*2] = currSymbol
            currSymbol = switchSymbol(currSymbol)
            printBoard()
    print("Player " + switchSymbol(currSymbol) + " won!")

main()
