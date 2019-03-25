#Print "Hello" (without the quotes)
#Print "Hello" (with the quotes)
#Create two variables, x and y, with the values 5 and 10, and print their sum
#Print "x plus y equals " followed by the sum of x and y
#Print a random number between 0 and 1
#Print a random integer between 0 and 20 (inclusive)
#Print a random integer between 1 and 20 (inclusive)

#Print 10 random numbers between 0 and 1
#Create a list of 10 random numbers between 0 and 1
#Create a list of 10 random numbers between 0 and 1 and count how many are less than 0.5
#Create a 10x10 2D list of random numbers between 0 and 1 and count how many are less than 0.5
#Create a 10x10 2D list of random numbers between 0 and 1 and print the sum of each row
#Print a pattern of asterisks:
# *
# **
# ***
# ****
# *****
#Print a pattern of asterisks:
#     *
#    **
#   ***
#  ****
# *****
#Implement BubbleSort again
#Schelling board
#Cellular automaton rule 26, rule 30


# for i in range(5):
#     print(random.randrange(10))
#     print("Printed " + str(i+1) + " random integers!")
# print("Done")

# alist = [10, 11]
# for i in range(5):
#     # alist.append(random.randrange(10))
#     alist.append(i)
# print(alist)
# print("Done")

import random

def prettyPrint(b):
    for i in range(len(b)):
        for j in range(len(b[i])):
            print(str(b[i][j]) + ' ', end='')
        print()

# alist=[]
# for i in range(5):
#     alist.append([])
#     for j in range(6):
#         alist[i].append(j)
# print(alist)
# prettyPrint(alist)


# for i in range(5):
#     for j in range(i+1):
#         print('*', end='')
#     print()

# for i in range(5):
#     print(random.randint(5,10))

for i in range(20):
    for j in range(20):
        randnum = random.random()
        if (randnum < 0.33):
            print('X ', end='')
        elif (randnum < 0.66):
            print('O ', end='')
        else:
            print('. ', end='')
    print()


# 
# 
# board=[]
# for i in range(20):
#     board.append([])
#     for j in range(20):
#         randnum = random.random()
#         if (randnum < 0.33):
#             board[i].append('X')
#         elif (randnum < 0.66):
#             board[i].append('O')
#         else:
#             board[i].append('.')
# 
# prettyPrint(board)