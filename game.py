import board
import time

def game():
    board1 = board.Board()
    end = True
    if board1.assign == "You":
        print(board1)
    while end:
        if board1.assign == "You":
            print("Your move.")
            while True:
                user_input = int(input("Enter your move: "))
                if board1.place(user_input) == False:
                    print("That place is taken. Try again.")
                else:
                    break
            print(board1)
        else:
            print("My turn.\n")
            time.sleep(2)
            board1.botMove()
            print(board1)

        check_end = board1.check_end()
        if check_end == -1:
            print("You have drawed.")
            end = False
        elif check_end == 1:
            print("You win.")
            end = False
        elif check_end == 0:
            print("You lost.")
            end = False