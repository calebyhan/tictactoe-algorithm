import board

I = input
# 

def game():
    board1 = board.Board()
    while not board1.end:
        if board1.assign == "You":
            print("Your move.")
            board1.place(int(I("Enter your move: ")))
            print(board1)
        else:
            print("My turn.")
            board1.botMove()
            print(board1)


    