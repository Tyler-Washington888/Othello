class Othello_Board:
    def __init__(self):
        self.board = [['', '', '', '', '', '', '', ''] for _ in range(8)]

    def print_board(self):
        for row in self.board:
            print(row)