def wincheck(gameboard, char, p):
    if gameboard[0] == char and gameboard[1] == char and gameboard[2] == char or gameboard[3] == char and gameboard[4] == char and gameboard[5] == char or gameboard[6] == char and gameboard[7] == char and gameboard[8] == char or gameboard[0] == char and gameboard[3] == char and gameboard[6] == char or gameboard[1] == char and gameboard[4] == char and gameboard[7] == char or gameboard[2] == char and gameboard[5] == char and gameboard[8] == char or gameboard[0] == char and gameboard[4] == char and gameboard[8] == char or gameboard[2] == char and gameboard[4] == char and gameboard[6] == char: input("\n" + p + " wins."); return True
    elif ' ' not in gameboard: input("\nTie."); return True
def move(gameboard, char, p, lonely, turn):
    print("\n" + p + ", choose a tile."); movemode, pmove = 'cpu' if lonely <= turn else 'hum', True
    while pmove == True:
        move = random.randint(0,8) if movemode == 'cpu' else int(input(">>> ")) -1
        if move < 8 or move > 0 and gameboard[move] == ' ': gameboard[move], pmove = char, False
def charchoose(p):
    while True:
        pchar = input("\nPlease enter " + p + "'s symbol\n>>> ")
        if len(pchar) == 1: return pchar
lonely = 69;
while lonely < 0 or lonely > 2: lonely = int(input("\nHow many players? (0/1/2)\n>>> "))
p1, p2 = "CPU2" if lonely == 0 else input("\nPlease enter player 1's name\n>>> "), "CPU1" if lonely != 2 else input("\nPlease enter player 2's name\n>>> "); import random; printboard, gameboard = lambda gameboard: print("\n" + gameboard[0] + " # " + gameboard[1] + " # " + gameboard[2] + "\n" + "#########\n" + gameboard[3] + " # " + gameboard[4] + " # " + gameboard[5] + "\n" + "#########\n" + gameboard[6] + " # " + gameboard[7] + " # " + gameboard[8]), [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']; win, turn = False, random.randint(0,1)
while True:
    p1char, p2char = charchoose(p1) if lonely != 0 else "0", charchoose(p2) if lonely == 2 else "x"
    if p1char != p2char: break
while win != True:
    printboard(gameboard); move(gameboard, p1char if turn == 0 else p2char, p1 if turn == 0 else p2, lonely, turn); turn = 1 if turn == 0 else 0
    if wincheck(gameboard, p1char, p1) == True or wincheck(gameboard, p2char, p2) == True or ' ' not in gameboard: win = True