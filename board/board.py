from typing import List


class Othello_Board:
    def __init__(self):
        self.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] for _ in range(8)]

        self.board[3][4] = self.board[4][3] = 'B'
        self.board[3][3] = self.board[4][4] = 'W'

        self.black_coordinates = {(3,4): True, (4,3): True}
        self.white_coordinates = {(3,3): True, (4,4): True}

        self.black_valid_moves = {(3,2): [], (2,3): [], (4,5): [], (5,4): []}
        self.white_valid_moves = {}

        self.turn_tracker = 'B'

    def update_board(self, starting_coord: tuple) -> None:
        coordinates_to_add = None
        coordinates_to_delete = None
        valid_moves = None
        piece = None

        if self.turn_tracker == "B":
            coordinates_to_add = self.black_coordinates
            coordinates_to_delete = self.white_coordinates
            valid_moves = self.black_valid_moves
            piece = "B"
        else:
            coordinates_to_add = self.white_coordinates
            coordinates_to_delete = self.black_coordinates
            valid_moves = self.white_valid_moves
            piece = "W"

        self.board[starting_coord[0]][starting_coord[1]] = piece
        coordinates_to_add[(starting_coord[0], starting_coord[1])] = True 

        for coord in valid_moves[starting_coord]:
            self.board[coord[0]][coord[1]] = piece
            coordinates_to_add[(coord[0], coord[1])] = True 
            del coordinates_to_delete[(coord[0], coord[1])]
    
    def find_valid_moves(self) -> None:
        valid_moves = None
        coorindates_to_check = None
        piece = None

        if self.turn_tracker == "B":
            valid_moves = self.black_valid_moves
            coorindates_to_check = self.white_coordinates
            piece = 'B'
        else:
            valid_moves = self.white_valid_moves
            coorindates_to_check  = self.black_coordinates
            piece = 'W'
        
        valid_moves.clear()

        for coordinate in coorindates_to_check:
            x = coordinate[0]
            y = coordinate[1]

            # check left of coordinate
            if (y - 1 >= 0) and (self.board[x][y - 1] == ' '):
                sequence_of_pieces = piece
                pieces_that_would_change = []
                yRef = y

                while yRef < 8 and self.board[x][yRef] != ' ':
                    sequence_of_pieces += self.board[x][yRef]
                    if self.board[x][yRef] != piece:
                        pieces_that_would_change.append((x, yRef))
                    yRef += 1

                first_piece = sequence_of_pieces[0]
                last_piece = sequence_of_pieces[len(sequence_of_pieces) - 1]
                middle_pieces = sequence_of_pieces[1:len(sequence_of_pieces) - 1] if len(sequence_of_pieces) > 2 else None

                print(sequence_of_pieces)

                if (first_piece == piece and last_piece == piece) and (middle_pieces and middle_pieces.find(piece) == -1):
                    valid_moves[(x, y - 1)] = pieces_that_would_change

            # check upper left of coordinate
            if (x - 1 >= 0) and (y - 1 >= 0) and (self.board[x - 1][y - 1] == ' '):
                sequence_of_pieces = piece
                pieces_that_would_change = []
                xRef = x
                yRef = y

                while xRef < 8 and yRef < 8 and self.board[xRef][yRef] != ' ':
                    sequence_of_pieces += self.board[xRef][yRef]
                    if self.board[xRef][yRef] != piece:
                        pieces_that_would_change.append((x, yRef))
                    xRef += 1
                    yRef += 1
                
                first_piece = sequence_of_pieces[0]
                last_piece = sequence_of_pieces[len(sequence_of_pieces) - 1]
                middle_pieces = sequence_of_pieces[1:len(sequence_of_pieces) - 1] if len(sequence_of_pieces) > 2 else None

                if (first_piece == piece and last_piece == piece) and (middle_pieces and middle_pieces.find(piece) == -1):
                    valid_moves[(x - 1, y - 1)] = pieces_that_would_change
                
            # check above coordinate
            if (x - 1 >= 0) and (self.board[x - 1][y] == ' '):
                sequence_of_pieces = piece
                pieces_that_would_change = []
                xRef = x

                while xRef < 8 and self.board[xRef][y] != ' ':
                    sequence_of_pieces += self.board[xRef][y]
                    if self.board[xRef][y] != piece:
                        pieces_that_would_change.append((xRef, y))
                    xRef += 1

                first_piece = sequence_of_pieces[0]
                last_piece = sequence_of_pieces[len(sequence_of_pieces) - 1]
                middle_pieces = sequence_of_pieces[1:len(sequence_of_pieces) - 1] if len(sequence_of_pieces) > 2 else None

                if (first_piece == piece and last_piece == piece) and (middle_pieces and middle_pieces.find(piece) == -1):
                    valid_moves[(x - 1, y)] = pieces_that_would_change

            # check upper right of coordinate
            if (x - 1 >= 0) and (y + 1 < 8) and (self.board[x - 1][y + 1] == ' '):
                sequence_of_pieces = piece
                pieces_that_would_change = []
                xRef = x
                yRef = y

                while xRef < 8 and yRef >= 0 and self.board[xRef][yRef] != ' ':
                    sequence_of_pieces += self.board[xRef][yRef]
                    if self.board[xRef][yRef] != piece:
                        pieces_that_would_change.append([xRef, yRef])
                    xRef += 1
                    yRef -= 1

                first_piece = sequence_of_pieces[0]
                last_piece = sequence_of_pieces[len(sequence_of_pieces) - 1]
                middle_pieces = sequence_of_pieces[1:len(sequence_of_pieces) - 1] if len(sequence_of_pieces) > 2 else None

                if (first_piece == piece and last_piece == piece) and (middle_pieces and middle_pieces.find(piece) == -1):
                    valid_moves[(x - 1, y + 1)] = pieces_that_would_change

            # check right of coordinate
            if (y + 1 < 8) and (self.board[x][y + 1] == ' '):
                sequence_of_pieces = piece
                pieces_that_would_change = []
                yRef = y

                while yRef >= 0 and self.board[x][yRef] != ' ':
                    sequence_of_pieces += self.board[x][yRef]
                    if self.board[x][yRef] != piece:
                        pieces_that_would_change.append((xRef, yRef))
                    yRef -= 1

                first_piece = sequence_of_pieces[0]
                last_piece = sequence_of_pieces[len(sequence_of_pieces) - 1]
                middle_pieces = sequence_of_pieces[1:len(sequence_of_pieces) - 1] if len(sequence_of_pieces) > 2 else None

                if (first_piece == piece and last_piece == piece) and (middle_pieces and middle_pieces.find(piece) == -1):
                    valid_moves[(x, y + 1)] = pieces_that_would_change

            # check bottom right of coordinate
            if (x + 1 < 8) and (y + 1 < 8) and (self.board[x + 1][y + 1] == ' '):
                sequence_of_pieces = piece
                pieces_that_would_change = []
                xRef = x
                yRef = y

                while xRef >= 0 and yRef >= 0 and self.board[xRef][yRef] != ' ':
                    sequence_of_pieces += self.board[xRef][yRef]
                    if self.board[xRef][yRef] != piece:
                        pieces_that_would_change.append((xRef, yRef))
                    xRef -= 1
                    yRef -= 1

                first_piece = sequence_of_pieces[0]
                last_piece = sequence_of_pieces[len(sequence_of_pieces) - 1]
                middle_pieces = sequence_of_pieces[1:len(sequence_of_pieces) - 1] if len(sequence_of_pieces) > 2 else None

                if (first_piece == piece and last_piece == piece) and (middle_pieces and middle_pieces.find(piece) == -1):
                    valid_moves[(x + 1, y + 1)] = pieces_that_would_change

            # check below coordinate
            if (x + 1 < 8) and (self.board[x + 1][y] == ' '):
                sequence_of_pieces = piece
                pieces_that_would_change = []
                xRef = x

                while xRef >= 0 and self.board[xRef][y] != ' ':
                    sequence_of_pieces += self.board[xRef][y]
                    if self.board[xRef][y] != piece:
                        pieces_that_would_change.append((xRef, y))
                    xRef -= 1

                first_piece = sequence_of_pieces[0]
                last_piece = sequence_of_pieces[len(sequence_of_pieces) - 1]
                middle_pieces = sequence_of_pieces[1:len(sequence_of_pieces) - 1] if len(sequence_of_pieces) > 2 else None

                if (first_piece == piece and last_piece == piece) and (middle_pieces and middle_pieces.find(piece) == -1):
                    valid_moves[(x + 1, y)] = pieces_that_would_change

            # check bottom left of coordinate
            if (x + 1 < 8) and (y - 1 >= 0) and (self.board[x + 1][y - 1] == ' '):
                sequence_of_pieces = piece
                pieces_that_would_change = []
                xRef = x
                yRef = y

                while xRef >= 0 and yRef < 8 and self.board[xRef][yRef] != ' ':
                    sequence_of_pieces += self.board[xRef][yRef]
                    if self.board[xRef][yRef] != piece:
                        pieces_that_would_change.append((xRef, yRef))
                    xRef -= 1
                    yRef += 1

                first_piece = sequence_of_pieces[0]
                last_piece = sequence_of_pieces[len(sequence_of_pieces) - 1]
                middle_pieces = sequence_of_pieces[1:len(sequence_of_pieces) - 1] if len(sequence_of_pieces) > 2 else None

                if (first_piece == piece and last_piece == piece) and (middle_pieces and middle_pieces.find(piece) == -1):
                    valid_moves[(x + 1, y - 1)] = pieces_that_would_change

    def print_board(self) -> None:
        for row in self.board:
            print("|".join(row))
            print('-' * 15)