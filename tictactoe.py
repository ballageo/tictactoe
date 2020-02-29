from os import system

#game functionality 
def printBoard():
    print ('''
     {} | {} | {}
    ===========
     {} | {} | {}
    ===========
     {} | {} | {}
        '''.format(gameboard[1], gameboard[2], gameboard[3], gameboard[4], gameboard[5], gameboard[6], gameboard[7], gameboard[8], gameboard[9]))

def horzWin(x, piece):
    if gameboard[x] == piece and gameboard[x+1] == piece and gameboard[x+2] == piece:
        return True
def vertWin(x, piece):
    if gameboard[x] == piece and gameboard[x+3] == piece and gameboard[x+6] == piece:
        return True
def diag1Win(piece):
    if gameboard[1] == piece and gameboard[5] == piece and gameboard[9] == piece: 
        return True
def diag2Win(piece):
    if gameboard[3] == piece and gameboard[5] == piece and gameboard[7] == piece: 
        return True
def draw(gameboard):
    free = []
    for i in gameboard:
        if i == " ":
            free.append(i)
    if len(free) == 1:
        return True


#setup for game
system("cls")
gameboard = [" "," "," "," "," "," "," "," "," "," "]
print ('''\nHello and welcome to the greatest tic-tac-toe game!
This will be the arena!\n
 {spot1} | {spot2} | {spot3}
===========
 {spot4} | {spot5} |{spot6}
===========
 {spot7} | {spot8} |{spot9}
\nFrom top-left to bottom-right, enter 1-9 to select a tile!
Who are our lovely contestants?'''.format(spot1=gameboard[1], spot2=gameboard[2], spot3=gameboard[3], spot4=gameboard[4], spot5=gameboard[5], spot6=gameboard[6], spot7=gameboard[7], spot8=gameboard[8], spot9=gameboard[9]))
player1 = raw_input("Player 1? \n")
player2 = raw_input("Player 2? \n")

legal_moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
turn = 1
error = 0
end = 0
player = player1

# while loop for game logic
while 1:
    if error == 1:
        system('cls')
        print("\nThat's the wrong move, partner! Pick an actual spot on that there board.")
        error = 0
    elif error == 2:
        system("cls")
        print("\nYou can't just go and take over spaces! This isn't the wild, wild west!")
        error = 0
    else:
        system('cls')
    if turn == 1:
        piece = "X"
    else:
        piece = "O"
    printBoard()
    choice = raw_input("It's {}'s turn! Which square do you want to pick? \n".format(player))
    if choice not in legal_moves:
        error = 1
        continue
    selection = int(choice)
    if gameboard[selection] != " ":
        error = 2
        continue
    gameboard[selection]=piece
    if horzWin(1, piece) or horzWin(4, piece) or horzWin(7, piece):
        break
    if vertWin(1, piece) or vertWin(2, piece) or vertWin(3, piece):
        break
    if diag1Win(piece):
        break
    if diag2Win(piece):
        break
    if draw(gameboard):
        end = 1
        break
    if turn == 1:
        turn = 2
        player = player2
    else:
        turn = 1
        player = player1
system("cls")
printBoard()
if end == 0:
    print("{} WINS!!!".format(player))
else:
    print("It's a draw!! Better luck next time!")
