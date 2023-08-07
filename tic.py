import sys
board=["-","-","-",
       "-","-","-",
       "-","-","-"]
def printboard(board):
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])
def winner(board):
    if (board[0] == board[1] and board[0] == board[2]):
        if board[0]=="x":
            print("winner is X")
            exit()
        elif board[0]=="o":
            print("winner is o")
            exit()
            
    elif (board[0] == board[3] and board[0] == board[6]):
        if board[0]=="x":
            print("winner is X")
            exit()
        elif board[0]=="o":
            print("winner is o")
            exit()
    elif (board[3] == board[4] and board[3] == board[5]):
        if board[3]=="x":
            print("winner is X")
            exit()
        elif board[0]=="o":
            print("winner is o")
            exit()
    elif (board[2] == board[5] and board[2] == board[8]):
        if board[2]=="x":
            print("winner is X")
            exit()
        elif board[2]=="o":
            print("winner is o")
            exit()
    elif (board[0] == board[4] and board[0] == board[8]):
        if board[0]=="x":
            print("winner is X")
            exit()
        elif board[0]=="o":
            print("winner is o")
            exit() 
    elif (board[2] == board[4] and board[0] == board[6]):
        if board[2]=="x":
            print("winner is X")
            exit()
        elif board[2]=="o":
            print("winner is o")
            exit()
    elif (board[1] == board[4] and board[1] == board[7]):
        if board[1]=="x":
            print("winner is X")
            exit()
        elif board[1]=="o":
            print("winner is o")
            exit()
    
def players_2(board):
    while True:
        try:
            player_2=int(input("enter number: "))
            if player_2<0 or player_2>8:
                print("wrong number")
                players_2(board)
            elif player_2>=0 or player_2<=8:
                if board[player_2]=="-":
                    board[player_2]="o"
                    printboard(board)
                    break
                else:
                    print("select right number")
                    players_2(board)
        except:
            print("wrong number")
            players_2(board)
        
def player(board):
    while True:
        try:
            player_1=int(input("enter number:"))
            if player_1<0 or player_1>8:
                print("wrong number")
                player(board)
            elif player_1>=0 or player_1<=8:
                if board[player_1]=="-":
                    board[player_1]="x"
                    printboard(board)
                    break
                    
                    
                else:
                    print("select right number")
                    player(board)
        except:
            print("wrong number")
            player(board)

            
while True:
    player(board)
    winner(board)
    players_2(board)
    winner(board)
    
