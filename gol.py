import array

#conway's game of life functions for use with attractorDots.py

#use 2 2d arrays to hold values for cell grid
# def initializeBoard(width, height):
#     board = [[0 for i in range(2)] for j in range(numPts)]

#ENDS: all dead, no change
# At each step in time, the following transitions occur:

# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
# These rules, which compare the behavior of the automaton to real life, can be condensed into the following:

# Any live cell with two or three live neighbours survives.
# Any dead cell with three live neighbours becomes a live cell.
# All other live cells die in the next generation. Similarly, all other dead cells stay dead.

def updateBoard(board):
    newBoard = board

    change = True
    dim = len(board)
    neighbors = 0   
    for i in range(dim):
        for j in range(len(dim)):
                neighbors = (board[(i - 1) % dim][(j - 1) % dim] + board[i][(j - 1) % dim] + board[(i + 1) % dim][(j - 1) % dim] +
                            board[(i - 1) % dim][j] + board[(i + 1) % dim][j] +
                            board[(i - 1) % dim][(j + 1) % dim] + board[i][(j + 1) % dim] + board[(i + 1) % dim][(j + 1) % dim])
                if board[i][j] == 1:
                    if (neighbors < 2) | (neighbors > 3):
                        newBoard[i][j] = 0
                else: # dead cell
                    if neighbors == 3:
                        newBoard[i][j] = 1
    if board == newBoard:
        change = False
    
    return newBoard, change
    