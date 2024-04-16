from Config import *
#from Func import *
from Figures import *


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        self.King_x = 0
        self.King_y = 4
        for row in range(8):
            self.field.append([None] * 8)
        self.field[0] = [
            Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
            King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)
        ]
        self.field[1] = [
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)
        ]
        self.field[6] = [
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)
        ]
        self.field[7] = [
            Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
            King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)
        ]

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def get_piece(self, row, col):
        if correct_coords(row, col):
            return self.field[row][col]
        else:
            return None

    def move_piece(self, row, col, row1, col1):
        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if self.field[row1][col1] is None:
            if not piece.can_move(self, row, col, row1, col1):
                return False
        elif self.field[row1][col1].get_color() == opponent(piece.get_color()):
            if not piece.can_attack(self, row, col, row1, col1):
                return False
        else:
            return False
        if isinstance(self.field[row][col], Rook):
            self.field[row][col].non_step = False
        if isinstance(self.field[row][col], Pawn) and row in [1, 6] and row1 in [0, 7]:
            Board.move_and_promote_pawn(self, row, col, row1, col1)
        if isinstance(self.field[row][col], King) and isinstance(self.field[row][col + 3], Rook) and self.field[row][col + 3].non_step and col1 == 6:
            return Board.castling7(self, row1)
        if isinstance(self.field[row][col], King) and isinstance(self.field[row][col - 4], Rook) and self.field[row][col - 4].non_step and col1 == 1:
            return Board.castling0(self, row1)
        else:
            self.field[row][col] = None
            self.field[row1][col1] = piece
            self.color = opponent(self.color)
        return True

    def move_and_promote_pawn(self, row, col, row1, col1):
        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row not in [1, 2, 3, 4, 5, 6]:
            return False
        piece = self.field[row][col]
        if piece is None:
            return False
        if not isinstance(piece, Pawn):
            return False
        color = piece.get_color()
        if color == WHITE:
            if row1 != 7:
                return False
        else:
            if row1 != 0:
                return False
        flag1 = piece.can_move(self, row, col, row1, col1) and self.field[row1][col1] is None
        flag2 = piece.can_attack(self, row, col, row1, col1) and self.field[row1][col1] is not None
        if flag1 or flag2:
            self.field[row][col] = None
            self.field[row1][col1] = Queen(color)
            self.color = opponent(self.color)
            return True
        return False

    def castling0(self, row1):
        if isinstance(self.field[row1][4], King):
            if isinstance(self.field[row1][0], Rook):
                if self.field[row1][1] is None:
                    if self.field[row1][2] is None:
                        if self.field[row1][3] is None:
                            self.field[row1][0] = None
                            self.field[row1][3] = Rook(self.color)
                            self.field[row1][3].non_step = False
                            self.field[row1][4] = None
                            self.field[row1][2] = King(self.color)
                            self.color = opponent(self.color)
                            return True
        return False

    def castling7(self, row1):
        if isinstance(self.field[row1][4], King):
            if isinstance(self.field[row1][7], Rook):
                if self.field[row1][5] is None:
                    if self.field[row1][6] is None:
                        self.field[row1][7] = None
                        self.field[row1][5] = Rook(self.color)
                        self.field[row1][5].non_step = False
                        self.field[row1][4] = None
                        self.field[row1][6] = King(self.color)
                        self.color = opponent(self.color)
                        return True
        return False

    def is_under_attack(self, row, col, color):
        for row1 in range(8):
            for col1 in range(8):
                if isinstance(self.field[row1][col1], Rook):
                    if self.field[row1][col1].get_color() == color:
                        if self.field[row1][col1].can_move(self, row1, col1, row, col):
                            return True
                if isinstance(self.field[row1][col1], Pawn):
                    if self.field[row1][col1].get_color() == color:
                        if self.field[row1][col1].can_move(self, row1, col1, row, col):
                            return True
                if isinstance(self.field[row1][col1], Queen):
                    if self.field[row1][col1].get_color() == color:
                        if self.field[row1][col1].can_move(self, row1, col1, row, col):
                            return True
                if isinstance(self.field[row1][col1], Bishop):
                    if self.field[row1][col1].get_color() == color:
                        if self.field[row1][col1].can_move(self, row1, col1, row, col):
                            return True
                if isinstance(self.field[row1][col1], Knight):
                    if self.field[row1][col1].get_color() == color:
                        if self.field[row1][col1].can_move(self, row1, col1, row, col):
                            return True
        return False