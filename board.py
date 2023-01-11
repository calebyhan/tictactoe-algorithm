import random

class Board:
    """
    Board key:
        -1: empty
        0: O
        1: X
    """

    def __init__(self):
        """
        Sets up the board with an empty board and variables
        """

        self.board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        self.turn = random.choice(["X", "O"])
        self.assign = random.choice(["You", "Bot"])
        self.end = False
    
    def __str__(self):
        board = []
        for i in self.board:
            board.append("{} | {} | {}\n".format(i[0], i[1], i[2]))
            board.append("---------\n")
        board = "".join(board[:-1])
        print(board)
        board = board.replace("-1", " ")
        return board

    def switch(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"
        if self.assign == "You":
            self.assign = "Bot"
        else:
            self.assign = "You"

    def check_end(self):
        cases = []

    def place(self, pos):
        x = pos % 3
        y = pos // 3
        if self.board[x][y] != -1:
            self.board[x][y] = self.turn
        self.switch()