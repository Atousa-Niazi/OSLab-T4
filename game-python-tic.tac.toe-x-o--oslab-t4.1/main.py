# Atousa Niazi Abkoh-98440127-Game-python-Tic.tac.toe(X,O)-OSLab

import random
import time

# zamany ke ba in def ha chap mishe beham mrize
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))

def computer(row_col):
    print('\ncomputer:') 
    while True:
        row=random.randint(0,3)
        col=random.randint(0,3)
        if 0<= row<=2 and 0<=col<=2:
            if game[row][col]=='-':
                game[row][col]='o'
                row_col[0]=row
                row_col[1]=col
                return row_col
                break
    print()
    
    
def Game_Board():
    print()
    print('--------------------')
    for i in range(3):
        for j in range(3):
            print(game[i][j],end='\t')
        print()
    print('--------------------')
def player_1(row_col):
    print('\nplayer_1:') 
    while True:
        print('row: ')
        row=int(input())
        print('colum: ')
        col=int(input())
        if 0<= row<=2 and 0<=col<=2:
            if game[row][col]=='-':
                game[row][col]='x'
                row_col[0]=row
                row_col[1]=col
                return row_col
                break
            else :
                print('occupied place,try again!')
        else :
            print('invalid input (row or colum must be 0-2)!!')
    print()
def player_2(row_col):
    print('\nplayer_2:')
    while True:
        print('row: ')
        row=int(input())
        print('colum: ')
        col=int(input())
        if 0<= row<=2 and 0<=col<=2:
            if game[row][col]=='-':
                game[row][col]='o'
                row_col[0]=row
                row_col[1]=col
                return row_col
                break
            else :
                print('occupied place,try again!')
        else :
            print('invalid input (row or colum must be 0-2)!!')
    print()
#check
def End_Game(game,row_col):
    count_x=0
    count_o=0
    row=row_col[0]
    col=row_col[1]
    if True==any('x' in sublist for sublist in game):
        if True==any('o' in sublist for sublist in game):
            if game[0][col]==game[1][col]==game[2][col]:
                if game[0][col]=='x':
                    print('player_1 wins')
                    return 0
                elif game[0][col]=='o':
                    print('player_2 wins')
                    return 0
            elif game[row][0] == game[row][1] == game[row][2]:
                if game[row][0]=='x':
                    print('player_1 wins')
                    return 0
                elif game[row][0]=='o':
                    print('player_2 wins')
                    return 0
            elif row == col and game[0][0] == game[1][1] ==game [2][2]:
                if game[0][0]=='x':
                    print('player_1 wins')
                    return 0
                elif game[0][0]=='o':
                    print('player_2 wins')
                    return 0
            elif row + col == 2 and game[0][2] == game[1][1] == game[2][0]:
                if game[0][2]=='x':
                    print('player_1 wins')
                    return 0
                elif game[0][2]=='o':
                    print('player_2 wins')
                    return 0
            if False==any('-' in sublist for sublist in game):
                print('draw!')
                return 0
    
game = [['-','-','-'],
        ['-','-','-'],
        ['-','-','-']]

print('wellcome!')
print('number of players:')
print(' 1 player : (1)')
print(' 2 player : (2)')
n=int(input())
Game_Board()

while n==1:
    row_col=[0,0]
    player_1(row_col)
    Game_Board()
    a=End_Game(game,row_col)
    if a ==0:
        print(time.time())
        break
    computer(row_col)
    Game_Board()
    a=End_Game(game,row_col)
    if a ==0:
        print(time.time())
        break
    

while n==2:
    row_col=[0,0]
    player_1(row_col)
    Game_Board()
    a=End_Game(game,row_col)
    if a ==0:
        print(time.time())
        break
    player_2(row_col)
    Game_Board()
    a=End_Game(game,row_col)
    if a ==0:
        print(time.time())
        break
    
    
    
    
    


