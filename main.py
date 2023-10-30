from board.board import Othello_Board

def main():
    othello_board = Othello_Board()
    othello_board.print_board()

    # while len(othello_board.black_valid_moves) or len(othello_board.white_valid_moves):
    #     othello_board.print_board()

    #     if othello_board.turn_tracker == 'B':
    #         print('It is player one\'s turn to place a black chip on the board')

    #         print(othello_board.black_valid_moves)

    #         validated_tuple = None

    #         while not validated_tuple:
    #             player_input = input('enter the keys, seperated by spaces, from the dictionary above to place a chip')
                
    #             unvalidated_tuple = tuple((int(x) for x in player_input.split()))

    #             if unvalidated_tuple in othello_board.black_valid_moves:
    #                 validated_tuple = unvalidated_tuple

    #             if not validated_tuple:
    #                 print('invalid entry')

    #         print('you choose to place a chip at ' + validated_tuple)

    #     else:
    #         print('It is player two\'s turn to place a white chip on the board')

if __name__ == "__main__":
    main()