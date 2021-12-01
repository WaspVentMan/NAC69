import random
def wincheck(gameboard, char, p):
    if gameboard[0] == char and gameboard[1] == char and gameboard[2] == char or gameboard[3] == char and gameboard[4] == char and gameboard[5] == char or gameboard[6] == char and gameboard[7] == char and gameboard[8] == char or gameboard[0] == char and gameboard[3] == char and gameboard[6] == char or gameboard[1] == char and gameboard[4] == char and gameboard[7] == char or gameboard[2] == char and gameboard[5] == char and gameboard[8] == char or gameboard[0] == char and gameboard[4] == char and gameboard[8] == char or gameboard[2] == char and gameboard[4] == char and gameboard[6] == char:
        print("\n" + p + " wins.")
        return True
def boardcheck(gameboard, p1char, p2char):
    for x in range(len(gameboard)):
        if gameboard[x] != ' ' and gameboard[x] != p1char and gameboard[x] != p2char:
            gameboard[x] = ' '
    printboard(gameboard)
def printboard(gameboard):
    print("\n" + gameboard[0] + " # " + gameboard[1] + " # " + gameboard[2] + "\n" + "#########\n" + gameboard[3] + " # " + gameboard[4] + " # " + gameboard[5] + "\n" + "#########\n" + gameboard[6] + " # " + gameboard[7] + " # " + gameboard[8])
def move(gameboard, char, p, lonely, turn):
    print("\n" + p + ", choose a tile.")
    if lonely <= turn:
        CPUmove(gameboard, char)
    else:
        playermove(gameboard, char)
def playermove(gameboard, char):
    pmove = True
    while pmove == True:
        move = int(input(">>> ")) -1
        if move > 8 or move < 0:
            print("Only numbers 1-9 are supported.")
        elif gameboard[move] == ' ':
            gameboard[move] = char
            pmove = False
def CPUmove(gameboard, char):
    pmove = True
    while pmove == True:
        move = random.randint(0,8)
        if gameboard[move] == ' ':
            gameboard[move] = char
            pmove = False
def charchoose(p):
    while True:
        pchar = input("\nPlease enter " + p + "'s symbol\n>>> ")
        if len(pchar) == 1:
            return pchar
gameboard = ['', '', '', '', '', '', '', '', '']
while True:
    lonely = int(input("\nHow many players? (0/1/2)\n>>> "))
    if lonely >= 0 and lonely <= 2:
        break
if lonely == 1 or lonely == 2:
    p1 = input("\nPlease enter player 1's name\n>>> ")
else:
    p1 = "CPU2"
p2 = "CPU1" if lonely != 2 else input("\nPlease enter player 2's name\n>>> ")
while True:
    if lonely == 2:
        p1char, p2char = charchoose(p1), charchoose(p2)
    if lonely == 1:
        p1char, p2char = charchoose(p1), "X"
    if lonely == 0:
        p1char, p2char = "O", "X"
    if p1char != p2char:
        break
win = False
turn = random.randint(0,1)
while win != True:
    boardcheck(gameboard, p1char, p2char)
    move(gameboard, p1char if turn == 0 else p2char, p1 if turn == 0 else p2, lonely, turn)
    if wincheck(gameboard, p1char, p1) == True or wincheck(gameboard, p2char, p2) == True or ' ' not in gameboard:
        if ' ' not in gameboard:
            print("\nTie.")
        win = True
    turn = 1 if turn == 0 else 0
input("\nThanks for Playing!") #nice