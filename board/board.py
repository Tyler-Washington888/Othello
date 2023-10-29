from typing import List


class Othello_Board:
    def __init__(self):
        self.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] for _ in range(8)]

        self.board[3][4] = self.board[4][3] = 'B'
        self.board[3][3] = self.board[4][4] = 'W'

        self.black_spots = [(3,4), (4,3)]
        self.white_spots = [(3,3), (4,4)] 

        self.black_valid_moves = {(3,2): True, (2,3): True, (4,5): True, (5,4): True}
        self.white_valid_moves = {}

        self.invalid_streak = 0

    def find_valid_moves(self, spots, piece):
        self.black_valid_moves.clear()

        for coordinate in spots:
            x = coordinate[0]
            y = coordinate[1]

            # check left of coordinate
            if (y - 1 >= 0) and (self.board[x][y - 1] == ' '):
                sequence_of_pieces = piece
                yRef = y

                while yRef < 8 and self.board[x][yRef] != ' ':
                    sequence_of_pieces += self.board[x][yRef]
                    yRef += 1

                first_piece = sequence_of_pieces[0]
                last_piece = sequence_of_pieces[len(sequence_of_pieces) - 1]
                middle_pieces = sequence_of_pieces[1:len(sequence_of_pieces) - 1] if len(sequence_of_pieces) > 2 else None

                if (first_piece == piece and last_piece == piece) and (middle_pieces and middle_pieces.find(piece) == -1):
                    if piece == 'B':
                        self.black_valid_moves[(x, y - 1)] = True
                    else:
                        self.white_valid_moves[(x, y - 1)] = True

            # check upper lett coordinate
            if (x - 1 >= 0) and (y - 1 >= 0) and (self.board[x - 1][y - 1] == ' '):
                sequence_of_pieces = piece
                xRef = x
                yRef = y

                while xRef < 8 and yRef < 8 and self.board[xRef][yRef] != ' ':
                    sequence_of_pieces += self.board[xRef][yRef]
                    xRef += 1
                    yRef += 1
                
                first_piece = sequence_of_pieces[0]
                last_piece = sequence_of_pieces[len(sequence_of_pieces) - 1]
                middle_pieces = sequence_of_pieces[1:len(sequence_of_pieces) - 1] if len(sequence_of_pieces) > 2 else None

                if (first_piece == piece and last_piece == piece) and (middle_pieces and middle_pieces.find(piece) == -1):
                    if piece == 'B':
                        self.black_valid_moves[(x - 1, y - 1)] = True
                    else:
                        self.white_valid_moves[(x - 1, y - 1)] = True
                
            # check above coordinate
            if (x - 1 >= 0) and (self.board[x - 1][y] == ' '):
                sequence_of_pieces = piece
                xRef = x

                while xRef < 8 and self.board[xRef][y] != ' ':
                    sequence_of_pieces += self.board[xRef][y]
                    xRef += 1

                first_piece = sequence_of_pieces[0]
                last_piece = sequence_of_pieces[len(sequence_of_pieces) - 1]
                middle_pieces = sequence_of_pieces[1:len(sequence_of_pieces) - 1] if len(sequence_of_pieces) > 2 else None

                if (first_piece == piece and last_piece == piece) and (middle_pieces and middle_pieces.find(piece) == -1):
                    if piece == 'B':
                        self.black_valid_moves[(x - 1, y)] = True
                    else:
                        self.white_valid_moves[(x - 1, y)] = True

            # check upper right of coordinate
            if (x - 1 >= 0) and (y + 1 < 8) and (self.board[x - 1][y + 1] == ' '):
                sequence_of_pieces = piece
                xRef = x
                yRef = y

                while xRef < 8 and yRef >= 0 and self.board[xRef][yRef] != ' ':
                    sequence_of_pieces += self.board[xRef][yRef]
                    xRef += 1
                    yRef -= 1

                first_piece = sequence_of_pieces[0]
                last_piece = sequence_of_pieces[len(sequence_of_pieces) - 1]
                middle_pieces = sequence_of_pieces[1:len(sequence_of_pieces) - 1] if len(sequence_of_pieces) > 2 else None

                if (first_piece == piece and last_piece == piece) and (middle_pieces and middle_pieces.find(piece) == -1):
                    if piece == 'B':
                        self.black_valid_moves[(x - 1, y + 1)] = True
                    else:
                        self.white_valid_moves[(x - 1, y + 1)] = True

            # check right of coordinate
            if (y + 1 < 8) and (self.board[x][y + 1] == ' '):
                sequence_of_pieces = piece
                yRef = y

                while yRef >= 0 and self.board[x][yRef] != ' ':
                    sequence_of_pieces += self.board[x][yRef]
                    yRef -= 1

                first_piece = sequence_of_pieces[0]
                last_piece = sequence_of_pieces[len(sequence_of_pieces) - 1]
                middle_pieces = sequence_of_pieces[1:len(sequence_of_pieces) - 1] if len(sequence_of_pieces) > 2 else None

                if (first_piece == piece and last_piece == piece) and (middle_pieces and middle_pieces.find(piece) == -1):
                    if piece == 'B':
                        self.black_valid_moves[(x, y + 1)] = True
                    else:
                        self.white_valid_moves[(x, y + 1)] = True

            # check bottom right of coordinate
            if (x + 1 < 8) and (y + 1 < 8) and (self.board[x + 1][y + 1] == ' '):
                sequence_of_pieces = piece
                xRef = x
                yRef = y

                while xRef >= 0 and yRef >= 0 and self.board[xRef][yRef] != ' ':
                    sequence_of_pieces += self.board[xRef][yRef]
                    xRef -= 1
                    yRef -= 1

                first_piece = sequence_of_pieces[0]
                last_piece = sequence_of_pieces[len(sequence_of_pieces) - 1]
                middle_pieces = sequence_of_pieces[1:len(sequence_of_pieces) - 1] if len(sequence_of_pieces) > 2 else None

                if (first_piece == piece and last_piece == piece) and (middle_pieces and middle_pieces.find(piece) == -1):
                    if piece == 'B':
                        self.black_valid_moves[(x + 1, y + 1)] = True
                    else:
                        self.white_valid_moves[(x + 1, y + 1)] = True

            # check below coordinate
            if (x + 1 < 8) and (self.board[x + 1][y] == ' '):
                sequence_of_pieces = piece
                xRef = x

                while xRef >= 0 and self.board[xRef][y] != ' ':
                    sequence_of_pieces += self.board[xRef][y]
                    xRef -= 1

                first_piece = sequence_of_pieces[0]
                last_piece = sequence_of_pieces[len(sequence_of_pieces) - 1]
                middle_pieces = sequence_of_pieces[1:len(sequence_of_pieces) - 1] if len(sequence_of_pieces) > 2 else None

                if (first_piece == piece and last_piece == piece) and (middle_pieces and middle_pieces.find(piece) == -1):
                    if piece == 'B':
                        self.black_valid_moves[(x + 1, y)] = True
                    else:
                        self.white_valid_moves[(x + 1, y)] = True

            # check bottom left of coordinate
            if (x + 1 < 8) and (y - 1 >= 0) and (self.board[x + 1][y - 1] == ' '):
                sequence_of_pieces = piece
                xRef = x
                yRef = y

                while xRef >= 0 and yRef < 8 and self.board[xRef][yRef] != ' ':
                    sequence_of_pieces += self.board[xRef][yRef]
                    xRef -= 1
                    yRef += 1

                
                first_piece = sequence_of_pieces[0]
                last_piece = sequence_of_pieces[len(sequence_of_pieces) - 1]
                middle_pieces = sequence_of_pieces[1:len(sequence_of_pieces) - 1] if len(sequence_of_pieces) > 2 else None

                if (first_piece == piece and last_piece == piece) and (middle_pieces and middle_pieces.find(piece) == -1):
                    if piece == 'B':
                        self.black_valid_moves[(x + 1, y - 1)] = True
                    else:
                        self.white_valid_moves[(x + 1, y - 1)] = True

    def print_board(self) -> None:
        for row in self.board:
            print("|".join(row))
            print('-' * 15)