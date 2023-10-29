from board.board import Othello_Board

def main():
    othello_board = Othello_Board()
    othello_board.print_board()
    othello_board.find_valid_moves(othello_board.white_coordinates, "B")

if __name__ == "__main__":
    main()