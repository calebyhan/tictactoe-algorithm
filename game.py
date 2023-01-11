import board
import time

def game():
    board1 = board.Board()
    print(board1)
    while not board1.end:
        if board1.assign == "You":
            print("Your move.")
            board1.place(int(input("Enter your move: ")))
        else:
            print("My turn.\n")
            time.sleep(2)
            board1.botMove()
            print(board1)


    