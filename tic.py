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
def player():
    while True:
        choose_player_1=int(input("choose from 0 to 8: "))
        if choose_player_1<0 or choose_player_1 >8:
            print("wrong number")
        else:
            if board[choose_player_1]=="-":
                board[choose_player_1]="x"
                printboard(board)
            else:
                while True:
                    choose_player_1=int(input("choose from 0 to 8: "))
                    if choose_player_1<0 or choose_player_1 >8:
                        print("wrong number")
                    else:
                            break
            
            winner(board)
            choose_player_2=int(input("choose from 0 to 8: "))
            if choose_player_2<0 or choose_player_2 >8:
                print("wrong number")
            else:
                while True:
                    if board[choose_player_2]=="-":
                        board[choose_player_2]="o"
                        printboard(board)
                    else:
                        printboard(board)
                        print("\nwrong numver\n")
                        choose_player_2=int(input("choose from 0 to 8: "))
                        if choose_player_2<0 or choose_player_2 >8:
                            print("wrong number")
                        else:
                            break
        
player()
