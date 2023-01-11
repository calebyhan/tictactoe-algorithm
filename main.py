import game

playAgain = "y"
print("\n Welcome to Tic-Tac-Toe. Place your marker by selecting a number on this refernce board, provided that the space is not occupied already. The board will be updated every turn. Have fun!\n")
print(" 0 | 1 | 2 \n-----------\n 3 | 4 | 5 \n-----------\n 6 | 7 | 8 \n")
while playAgain != "n":
    game.game()
    playAgain = input("Would you like to play again? (y/n): ")
