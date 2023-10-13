from classes.board import Othello_Board

def main():
    othello_board = Othello_Board()
    othello_board.board[3][5] = 'b'
    othello_board.print_board()

if __name__ == "__main__":
    main()