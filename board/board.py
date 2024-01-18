from typing import List


class Othello_Board:
    def __init__(self):
        self.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] for _ in range(8)]

        self.board[3][4] = self.board[4][3] = 'B'
        self.board[3][3] = self.board[4][4] = 'W'

        self.black_coordinates = {(3,4): True, (4,3): True}
        self.white_coordinates = {(3,3): True, (4,4): True}

        self.black_valid_moves = {}
        self.white_valid_moves = {}

        self.turn_tracker = 'B'
    
    def change_turn(self) -> None:
        if self.turn_tracker == 'B':
            self.turn_tracker = 'W'
        else:
            self.turn_tracker = 'B'

    def determine_winner(self) -> str:
        if len(self.black_coordinates) == len(self.white_coordinates):
            return 'tie'
        if len(self.black_coordinates) > len(self.white_coordinates):
            return 'black'
        else:
            return 'white'

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
                yRef = y

                while yRef < 8 and (self.board[x][yRef] != ' ' and self.board[x][yRef] != piece):
                    sequence_of_pieces += self.board[x][yRef]
                    yRef += 1

                if yRef < 8 and self.board[x][yRef] == piece: sequence_of_pieces += piece

                if len(sequence_of_pieces) > 2 and sequence_of_pieces[-1] == piece and sequence_of_pieces[1:-1].find(piece) == -1:
                    valid_moves[(x, y - 1)] = self.pieces_that_would_change(x, y - 1, piece)

            # check upper left of coordinate
            if (x - 1 >= 0) and (y - 1 >= 0) and (self.board[x - 1][y - 1] == ' '):
                sequence_of_pieces = piece
                xRef = x
                yRef = y

                while xRef < 8 and yRef < 8 and (self.board[xRef][yRef] != ' ' and self.board[xRef][yRef] != piece):
                    sequence_of_pieces += self.board[xRef][yRef]
                    xRef += 1
                    yRef += 1
                                
                if xRef < 8 and yRef < 8 and self.board[xRef][yRef] == piece: sequence_of_pieces += piece

                if len(sequence_of_pieces) > 2 and sequence_of_pieces[-1] == piece and sequence_of_pieces[1:-1].find(piece) == -1:
                    valid_moves[(x - 1, y - 1)] = self.pieces_that_would_change(x - 1, y - 1, piece)
                
            # check above coordinate
            if (x - 1 >= 0) and (self.board[x - 1][y] == ' '):
                sequence_of_pieces = piece
                xRef = x

                while xRef < 8 and (self.board[xRef][y] != ' ' and self.board[xRef][y] != piece):
                    sequence_of_pieces += self.board[xRef][y]
                    xRef += 1

                if xRef < 8 and self.board[xRef][y] == piece: sequence_of_pieces += piece

                if len(sequence_of_pieces) > 2 and sequence_of_pieces[-1] == piece and sequence_of_pieces[1:-1].find(piece) == -1:
                    valid_moves[(x - 1, y)] = self.pieces_that_would_change(x - 1, y, piece)

            # check upper right of coordinate
            if (x - 1 >= 0) and (y + 1 < 8) and (self.board[x - 1][y + 1] == ' '):
                sequence_of_pieces = piece
                xRef = x
                yRef = y

                while xRef < 8 and yRef >= 0 and (self.board[xRef][yRef] != ' ' and self.board[xRef][yRef] != piece):
                    sequence_of_pieces += self.board[xRef][yRef]
                    xRef += 1
                    yRef -= 1
                                
                if xRef < 8 and y >=0 and self.board[xRef][yRef] == piece: sequence_of_pieces += piece

                if len(sequence_of_pieces) > 2 and sequence_of_pieces[-1] == piece and sequence_of_pieces[1:-1].find(piece) == -1:
                    valid_moves[(x - 1, y + 1)] = self.pieces_that_would_change(x - 1, y + 1, piece)

            # check right of coordinate
            if (y + 1 < 8) and (self.board[x][y + 1] == ' '):
                sequence_of_pieces = piece
                yRef = y

                while yRef >= 0 and (self.board[x][yRef] != ' ' and self.board[x][yRef] != piece):
                    sequence_of_pieces += self.board[x][yRef]
                    yRef -= 1

                if xRef < 8 and self.board[x][yRef] == piece: sequence_of_pieces += piece

                if len(sequence_of_pieces) > 2 and sequence_of_pieces[-1] == piece and sequence_of_pieces[1:-1].find(piece) == -1:
                    valid_moves[(x, y + 1)] = self.pieces_that_would_change(x, y + 1, piece)

            # check bottom right of coordinate
            if (x + 1 < 8) and (y + 1 < 8) and (self.board[x + 1][y + 1] == ' '):
                sequence_of_pieces = piece
                xRef = x
                yRef = y

                while xRef >= 0 and yRef >= 0 and (self.board[xRef][yRef] != ' ' and self.board[xRef][yRef] != piece):
                    sequence_of_pieces += self.board[xRef][yRef]
                    xRef -= 1
                    yRef -= 1

                if xRef >= 0 and yRef >= 0 and self.board[xRef][yRef] == piece: sequence_of_pieces += piece

                if len(sequence_of_pieces) > 2 and sequence_of_pieces[-1] == piece and sequence_of_pieces[1:-1].find(piece) == -1:
                    valid_moves[(x + 1, y + 1)] = self.pieces_that_would_change(x + 1, y + 1, piece)

            # check below coordinate
            if (x + 1 < 8) and (self.board[x + 1][y] == ' '):
                sequence_of_pieces = piece
                xRef = x

                while xRef >= 0 and (self.board[xRef][y] != ' ' and self.board[xRef][y] != piece):
                    sequence_of_pieces += self.board[xRef][y]
                    xRef -= 1

                if xRef >= 0 and self.board[xRef][y] == piece: sequence_of_pieces += piece

                if len(sequence_of_pieces) > 2 and sequence_of_pieces[-1] == piece and sequence_of_pieces[1:-1].find(piece) == -1:
                    valid_moves[(x + 1, y)] = self.pieces_that_would_change(x + 1, y, piece)

            # check bottom left of coordinate
            if (x + 1 < 8) and (y - 1 >= 0) and (self.board[x + 1][y - 1] == ' '):
                sequence_of_pieces = piece
                xRef = x
                yRef = y

                while xRef >= 0 and yRef < 8 and (self.board[xRef][yRef] != ' ' and self.board[xRef][yRef] != piece):
                    sequence_of_pieces += self.board[xRef][yRef]
                    xRef -= 1
                    yRef += 1


                if xRef >= 0 and yRef < 8 and self.board[xRef][yRef] == piece: sequence_of_pieces += piece

                if len(sequence_of_pieces) > 2 and sequence_of_pieces[-1] == piece and sequence_of_pieces[1:-1].find(piece) == -1:
                    print('hey')
                    print(self.pieces_that_would_change(x + 1, y -1, piece))
                    valid_moves[(x + 1, y - 1)] = self.pieces_that_would_change(x + 1, y -1, piece)

    def pieces_that_would_change(self, x:int, y:int, current_piece: str):
        pieces_that_would_change = []
        piece = current_piece

        # go right
        right_string = piece
        right_affected_pieces = []
        yRef = y + 1
        while yRef < 8 and (self.board[x][yRef] != ' ' and self.board[x][yRef] != piece):
            right_string += self.board[x][yRef]
            right_affected_pieces.append((x, yRef))
            yRef += 1
        
        if yRef < 8 and self.board[x][yRef] == piece: right_string += piece

        if len(right_string) > 2 and right_string[-1] == piece and right_string[1: - 1].find(piece) == -1:
            pieces_that_would_change.extend(right_affected_pieces)

        # go down and right
        up_right_string = piece
        up_right_affected_pieces = []
        xRef = x + 1
        yRef = y + 1

        while xRef < 8 and yRef < 8 and (self.board[xRef][yRef] != ' ' and self.board[xRef][yRef] != piece):
            up_right_string += self.board[xRef][yRef]
            up_right_affected_pieces.append((xRef, yRef))
            xRef += 1
            yRef += 1
         
        if xRef < 8 and yRef < 8 and self.board[xRef][yRef] == piece: up_right_string += piece

        if len(up_right_string) > 2 and up_right_string[-1] == piece and up_right_string[1: - 1].find(piece) == -1:
                pieces_that_would_change.extend(up_right_affected_pieces)

        # go down
        down_string = piece
        down_affected_pieces = []
        xRef = x + 1

        while xRef < 8 and (self.board[xRef][y] != ' ' and self.board[xRef][y] != piece):
            down_string += self.board[xRef][y]
            down_affected_pieces.append((xRef, y))
            xRef += 1
        
        if xRef < 8 and self.board[xRef][y] == piece: down_string += piece

        if len(down_string) > 2 and down_string[-1] == piece and down_string[1: - 1].find(piece) == -1:
            pieces_that_would_change.extend(down_affected_pieces)
    
        # go down and left
        down_left_string = piece
        down_left_affected_pieces = []
        xRef = x + 1
        yRef = y - 1

        while xRef < 8 and yRef >= 0 and (self.board[xRef][yRef] != ' ' and self.board[xRef][yRef] != piece):
            down_left_string += self.board[xRef][yRef]
            down_left_affected_pieces.append((xRef, yRef))
            xRef += 1
            yRef -= 1
         
        if xRef < 8 and yRef >= 0 and self.board[xRef][yRef] == piece: down_left_string += piece

        if len(down_left_string) > 2 and down_left_string[-1] == piece and down_left_string[1: - 1].find(piece) == -1:
            pieces_that_would_change.extend(down_left_affected_pieces)

        # go left
        left_string = piece
        left_affected_pieces = []
        yRef = y - 1

        while yRef >= 0 and (self.board[x][yRef] != ' ' and self.board[x][yRef] != piece):
            left_string += self.board[x][yRef]
            left_affected_pieces.append((x, yRef))
            yRef -= 1
        
        if yRef >= 0 and self.board[x][yRef] == piece: left_string += piece

        if len(left_string) > 2 and left_string[-1] == piece and left_string[1: - 1].find(piece) == -1:
            pieces_that_would_change.extend(left_affected_pieces)

        # up down and left
        up_left_string = piece
        up_left_affected_pieces = []
        xRef = x - 1
        yRef = y - 1

        while xRef >= 0 and yRef >= 0 and (self.board[xRef][yRef] != ' ' and self.board[xRef][yRef] != piece):
            up_left_string += self.board[xRef][yRef]
            up_left_affected_pieces.append((xRef, yRef))
            xRef -= 1
            yRef -= 1
         
        if xRef >= 0 and yRef >= 0 and self.board[xRef][yRef] == piece: up_left_string += piece

        if len(up_left_string) > 2 and up_left_string[-1] == piece and up_left_string[1: - 1].find(piece) == -1:
            pieces_that_would_change.extend(up_left_affected_pieces)

        # go up
        up_string = piece
        up_affected_pieces = []
        xRef = x - 1

        while xRef >= 0 and (self.board[xRef][y] != ' ' and self.board[xRef][y] != piece):
            up_string += self.board[xRef][y]
            up_affected_pieces.append((xRef, y))
            xRef -= 1
        
        if xRef >= 0 and self.board[xRef][y] == piece: up_string += piece

        if len(up_string) > 2 and up_string[-1] == piece and up_string[1: - 1].find(piece) == -1:
            pieces_that_would_change.extend(up_affected_pieces)

        # go up and right
        up_right_string = piece
        up_right_affected_pieces = []
        xRef = x - 1
        yRef = y + 1

        while xRef >= 0 and yRef < 8 and (self.board[xRef][yRef] != ' ' and self.board[xRef][yRef] != piece):
            up_right_string += self.board[xRef][yRef]
            up_right_affected_pieces.append((xRef, yRef))
            xRef -= 1
            yRef += 1
         
        if xRef >= 0 and yRef < 8 and self.board[xRef][yRef] == piece: up_right_string += piece

        if len(up_right_string) > 2 and up_right_string[-1] == piece and up_right_string[1: - 1].find(piece) == -1:
                pieces_that_would_change.extend(up_right_affected_pieces)
        
        return pieces_that_would_change
    
    def print_board(self) -> None:
        for row in self.board:
            print("|".join(row))
            print('-' * 15)