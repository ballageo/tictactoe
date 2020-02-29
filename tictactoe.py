from os import system
def startgame():
    gameboard = ['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    test1 = "Muahaha"
    print ('''Hello and welcome to the greatest tic-tac-toe game!
This will be the arena!
 {spot1} | {spot2} | {spot3}
===========
 {spot4} | {spot5} |{spot6}
===========
 {spot7} | {spot8} |{spot9}
From top-left to bottom-right, enter 1-9 to select a tile!
Who are our lovely contestants?'''.format(spot1=gameboard[1], spot2=gameboard[2], spot3=gameboard[3], spot4=gameboard[4], spot5=gameboard[5], spot6=gameboard[6], spot7=gameboard[7], spot8=gameboard[8], spot9=gameboard[9]))
    
    player1 = raw_input("Player 1? \n")
    player2 = raw_input("Player 2? \n")
    spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9 = gameboard[1], gameboard[2], gameboard[3], gameboard[4], gameboard[5], gameboard[6], gameboard[7], gameboard[8], gameboard[9]
    system("cls")
    print ("Wonderful!! {} goes first!\n".format(player1))
    while 1:
        system('cls')
        print ('''
 {spot1} | {spot2} | {spot3}
===========
 {spot4} | {spot5} |{spot6}
===========
 {spot7} | {spot8} |{spot9}
        '''.format(spot1=spot1, spot2=spot2, spot3=spot3, spot4=spot4, spot5=spot5, spot6=spot6, spot7=spot7, spot8=spot8, spot9=spot9))
        num = int(raw_input("Which square do you want to pick? \n"))
        if num == 1:
            spot1="X"
        if num == 12:
            break
    
startgame()
