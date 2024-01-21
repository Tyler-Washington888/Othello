from board.board import Othello_Board
from players.random_player import Random_Player

def main():
    othello_board = Othello_Board()
    othello_board.find_valid_moves()
    game_is_not_over = True


    player_two = None

    while not player_two:
        player_type = input('Tell us the opponent you want to play against (1: RandomPlayer, 2: Real Oppenent):')

        if player_type not in ['1', '2']:
            print('Your input was invalid, try again')
            print()
        else:
            player_two = player_type

    if player_two == '1': player_two = Random_Player()

    while game_is_not_over:
        othello_board.print_board()

        if othello_board.turn_tracker == 'B':
            print('Player One, it is your turn to place a black chip on the board at one of the following coordinates: ')
            print()

            print(othello_board.black_valid_moves)
            print()

            validated_tuple = None

            while not validated_tuple:
                player_input = input('Choose a coordinate by entering each value, seperated by spaces here:')

                unvalidated_tuple = tuple((int(x) for x in player_input.split()))

                if unvalidated_tuple in othello_board.black_valid_moves:
                    validated_tuple = unvalidated_tuple

                if not validated_tuple:
                    print('Your input was invalid, try again')
                    print()
                    print(othello_board.black_valid_moves)
                    print()

            othello_board.update_board(validated_tuple)

            print()
            print('Player One, you chose to place a chip at coordinate ' + str(validated_tuple))
            print('& this is what the board looks like now')
            print()
            
            # check if game is over
            othello_board.find_valid_moves()
            othello_board.change_turn()
            othello_board.find_valid_moves()

            if not(len(othello_board.white_valid_moves)):
                if len(othello_board.black_valid_moves):
                    othello_board.change_turn()
                else:
                    game_is_not_over = False

        else:
            validated_tuple = None

            if player_two == '2':
                print('Player Two, it is your turn to place a white chip on the board at one of the following coordinates: ')
                print()

                print(othello_board.white_valid_moves)
                print()

                while not validated_tuple:
                    player_input = input('Choose a coordinate by entering each value, seperated by spaces here:')

                    unvalidated_tuple = tuple((int(x) for x in player_input.split()))

                    if unvalidated_tuple in othello_board.white_valid_moves:
                        validated_tuple = unvalidated_tuple

                    if not validated_tuple:
                        print('Your input was invalid, try again')
                        print()
                        print(othello_board.white_valid_moves)
                        print()
            else:
                print(othello_board.white_valid_moves)
                validated_tuple = player_two.choose_move(othello_board.white_valid_moves)

            othello_board.update_board(validated_tuple)

            print()
            print('Player Two, you chose to place a chip at coordinate ' + str(validated_tuple))
            print('& this is what the board looks like now')
            print()
            
            # check if game is over
            othello_board.find_valid_moves()
            othello_board.change_turn()
            othello_board.find_valid_moves()

            if not(len(othello_board.black_valid_moves)):
                if len(othello_board.white_valid_moves):
                    othello_board.change_turn()
                else:
                    game_is_not_over = False

    winner = othello_board.determine_winner()

    if winner == 'black': print('Congrats Player One, you won the game')
    elif winner == 'white': print('Congrats Player Two, you won the game')
    else: print('The game ended in a tie')

    del othello_board
if __name__ == "__main__":
    main()