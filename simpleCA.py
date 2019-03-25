import random
import time

#This program generates a simple visualization of 1D cellular automata
NUM_COLS=100
MID_COL=int(NUM_COLS/2)
RULE=30

currentState = []
newState = []
nextState = {}

def initializeRule():
    if (RULE==26):
        print("Rule 26")
        #This dictionary encodes rule 26
        nextState = {
            '000': 0,
            '001': 1,
            '010': 0,
            '011': 1,
            '100': 1,
            '101': 0,
            '110': 0,
            '111': 0
        }        
    if (RULE==30):
        #This dictionary encodes Rule 30
        nextState = {
            '000': 0,
            '001': 1,
            '010': 1,
            '011': 1,
            '100': 1,
            '101': 0,
            '110': 0,
            '111': 0
        }
    return nextState

def initializeState():
    for i in range(NUM_COLS):
        currentState.append(0)
        newState.append(0)
    currentState[MID_COL]=1
    
def getState(x):
    state=''
    if (x==0):
        state = state+str(currentState[NUM_COLS-1])
    else:
        state = state+str(currentState[x-1])
    state = state+str(currentState[x])
    if (x==NUM_COLS-1):
        state = state+str(currentState[0])
    else:
        state = state+str(currentState[x+1])
    return state

def updateState():
    for i in range(NUM_COLS):
        state = getState(i)
        newState[i] = nextState[state]
        
        
        
## Main program
initializeState()
nextState = initializeRule()
for iteration in range(1000):
    for col in range(NUM_COLS):
        if (currentState[col]==1):
            print('*', end='')
        else:
            print(' ', end='')
    print()
    updateState()
    currentState = newState.copy()
    time.sleep(1) #Pause 1 second
