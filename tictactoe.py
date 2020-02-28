def startgame():
    gameboard = [[1,0,0],
                [0,0,2],
                [0,1,0]]
    print ("Hello and welcome to the greatest tic-tac-toe game!\n"
    "This will be the arena!\n"
    "_|_|_\n"
    "_|_|_\n"
    " | | \n"
    "From top-left to bottom-right, enter 1-9 to select a tile!\n"
    "Who are our lovely contestants?\n")
    
    player1 = raw_input("Player 1? \n")
    player2 = raw_input("Player 2? \n")
    
    print ("Wonderful!! {} goes first!\n".format(player1))
    
    while 1:
        num = int(raw_input("Which square do you want to pick? \n"))
        print ("lol you chose {} \n".format(num))
        if num == 12:
            break
    
startgame()
