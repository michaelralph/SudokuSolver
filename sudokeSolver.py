import time

""" Input: the board
    Outputs: empty tile coordinates
    nextEmptyTile finds the next empty tile and returns its coordinates. If
there are no empty tiles remaining, it returns -1, -1. """


def nextEmptyTile(board):
    for x in range(0, 9):
        for y in range(0, 9):
            if board[x][y] == 0:
                return x, y
    return -1, -1


""" Input: the board, x-coordinate (i), y-coordinate (j), potential number (e)
    Output: boolean
    validMove checks if a move is legal. It checks if there are any multiples
in a specific row, column, and quadrant. If a move can be made it returns 
True, else it returns False."""


def validMove(board, i, j, e):
    if e not in board[i]:
        checkColumn = True
        for x in range(9):
            if e == board[x][j]:
                checkColumn = False
        if checkColumn:
            secTopX, secTopY = 3 * (i//3), 3 * (j//3)
            for x in range(secTopX, secTopX + 3):
                for y in range(secTopY, secTopY + 3):
                    if board[x][y] == e:
                        return False
            return True
    return False


""" Input: the board, x-coordinate (i), y-coordinate (j)
    Output: solved Sudoku puzzle, and boolean
    sudokuSolver solves a Sudoku board using backtracking and recursion. It only solves
 solvable puzzles. Consider adding in a step that checks if puzzles are solvable or not."""


def sudokuSolver(board, i=0, j=0):
    i, j = nextEmptyTile(board)
    if i == -1:
        for num in range(0, 9):
            print(board[num])
        return True
    for e in range(1, 10):
        if validMove(board, i, j, e):
            board[i][j] = e
            if sudokuSolver(board, i, j):
                return True
            board[i][j] = 0
    return False


board = [[8,0,0,0,0,0,0,0,0],
         [0,0,3,6,0,0,0,0,0],
         [0,7,0,0,9,0,2,0,0],
         [0,5,0,0,0,7,0,0,0],
         [0,0,0,0,4,5,7,0,0],
         [0,0,0,1,0,0,0,3,0],
         [0,0,1,0,0,0,0,6,8],
         [0,0,8,5,0,0,0,1,0],
         [0,9,0,0,0,0,4,0,0]]

initialTime = time.clock()
sudokuSolver(board)
finalTime = time.clock()
print("Elapsed time: " + str(round((finalTime - initialTime), 4)) + " sec")
