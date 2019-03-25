import random
import time
from colorama import init, Back, Style
init()

NUM_ROWS = 20
NUM_COLS = 20
PX = 0.33
PO = 0.33
NUM_TIME_STEPS = 1000
HAPPINESS_THRESHOLD = 0.4
NEIGHBORHOOD_RANGE = 1

def prettyPrint(b, fromRow=-1, fromCol=-1, toRow=-1, toCol=-1):
    for i in range(len(b)):
        for j in range(len(b[i])):
            if (i==fromRow and j==fromCol):
                print(Back.BLUE + str(b[i][j]), end='')
                print(Style.RESET_ALL + ' ', end='')
            elif (i==toRow and j==toCol):
                print(Back.GREEN + str(b[i][j]), end='')
                print(Style.RESET_ALL + ' ', end='')
            else:
                print(str(b[i][j]) + ' ', end='')
        print()
        
def initialize():
    for i in range(NUM_ROWS):
        board.append([])
        for j in range(NUM_COLS):
            randnum = random.random()
            if (randnum < PX):
                board[i].append('X')
            elif (randnum < PX + PO):
                board[i].append('O')
            else:
                board[i].append('.')


#We will measure the average fraction of neighbors of each cell
#who are of the same type as that cell
def measureSegregation():
    sumOfFractions = 0
    totalCount = 0
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            # Count the number of Xs and Os in the neighborhood
            nbors = getNeighbors(i, j)
            nX, nO = countXO(nbors)
            
            if (board[i][j]=='X'):
                nX -= 1
            elif (board[i][j]=='O'):
                nO -= 1
            
            # Convert them into fractions
            if (nX==0 and nO==0):
                fractionX = 0
                fractionO = 0
            else:
                fractionX = nX/(nX + nO)
                fractionO = nO/(nX + nO)
            
            # Update the average
            if (board[i][j]=='X'):
                sumOfFractions += fractionX
                totalCount += 1
            elif (board[i][j]=='O'):
                sumOfFractions += fractionO
                totalCount += 1
                
    avgFraction = sumOfFractions/totalCount
    print(avgFraction)

def findNewLocation(h):
    while True:
        #Choose a random location
        r = random.randrange(NUM_ROWS)
        c = random.randrange(NUM_COLS)
        
        if (board[r][c]=='.'):
            # Count the number of Xs and Os in the neighborhood
            nbors = getNeighbors(r, c)
            nX, nO = countXO(nbors)
            # Convert them into fractions
            if (nX==0 and nO==0):
                fractionX = 0
                fractionO = 0
            else:
                fractionX = nX/(nX + nO)
                fractionO = nO/(nX + nO)
            if (h=='X'):
                if (fractionX > HAPPINESS_THRESHOLD):
                    return r, c
            if (h=='O'):
                if (fractionO > HAPPINESS_THRESHOLD):
                    return r, c
        


def getNeighbors(r, c):
    rowMin = r - NEIGHBORHOOD_RANGE
    rowMax = r + NEIGHBORHOOD_RANGE + 1
    colMin = c - NEIGHBORHOOD_RANGE
    colMax = c + NEIGHBORHOOD_RANGE + 1
    
    if (rowMin < 0):
        rowMin = 0
    if (rowMax > NUM_ROWS):
        rowMax = NUM_ROWS
    if (colMin < 0):
        colMin = 0
    if (colMax > NUM_COLS):
        colMax = NUM_COLS

    neighbors = []
    for i in range(rowMin, rowMax, 1):
        for j in range(colMin, colMax, 1):
            neighbors.append(board[i][j])
    
    return(neighbors)

def countXO(neighborList):
    numX = 0
    numO = 0
    for nbor in neighborList:
        if (nbor == 'X'):
            numX += 1
        if (nbor == 'O'):
            numO += 1
    return numX, numO

def updatePosition():
    # Choose a random location
    randRow = random.randrange(NUM_ROWS)
    randCol = random.randrange(NUM_COLS)
    
    # If it is a . skip
    if (board[randRow][randCol] == '.'):
        return
    
    # print("Random row = " + str(randRow))
    # print("Random column = " + str(randCol))
    # print("Value at that location: " + board[randRow][randCol])

    # Count the number of Xs and Os in the neighborhood
    nbors = getNeighbors(randRow, randCol)
    
    # print("Neighbors: " + str(nbors))
    
    nX, nO = countXO(nbors)
    if (board[randRow][randCol]=='X'):
        nX -= 1
    else:
        nO -= 1
    
    # print("Number of Xs in the neighborhood: " + str(nX))
    # print("Number of Os in the neighborhood: " + str(nO))
    
    # Convert them into fractions
    if (nX==0 and nO==0):
        fractionX = 0
        fractionO = 0
    else:
        fractionX = nX/(nX + nO)
        fractionO = nO/(nX + nO)
    
    # print("Fraction X in neighborhood = " + str(fractionX))
    # print("Fraction O in neighborhood = " + str(fractionO))
    
    # If the location has an X:
    if (board[randRow][randCol] == 'X'):
        #   if the fraction of Xs in the neighborhood < HAPPINESS_THRESHOLD:
        if (fractionX < HAPPINESS_THRESHOLD):
            #   Find a new location for this X where it would be happy
            newR, newC = findNewLocation('X')
            #   Move the X to the new location
            board[randRow][randCol] = '.'
            board[newR][newC] = 'X'
            # prettyPrint(board, randRow, randCol, newR, newC)
            # print()
    else:
        if (fractionO < HAPPINESS_THRESHOLD):
            newR, newC = findNewLocation('O')
            board[randRow][randCol] = '.'
            board[newR][newC] = 'O'
            # prettyPrint(board, randRow, randCol, newR, newC)
            # print()


###### Main program

board = []
initialize()
prettyPrint(board)

for i in range(NUM_TIME_STEPS):
    updatePosition()
    measureSegregation()
    
prettyPrint(board)
    
    