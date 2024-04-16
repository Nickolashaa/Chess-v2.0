WHITE = 1
BLACK = 2


def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE


def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


class Rook:

    def __init__(self, color):
        self.color = color
        self.non_step = True

    def get_color(self):
        return self.color

    def char(self):
        return '_Rook'

    def can_move(self, board, row, col, row1, col1):
        if row != row1 and col != col1:
            return False
        if row1 == row and col1 == col:
            return False

        step = 1 if (row1 >= row) else -1
        for r in range(row + step, row1, step):
            if not (board.get_piece(r, col) is None):
                return False

        step = 1 if (col1 >= col) else -1
        for c in range(col + step, col1, step):
            if not (board.get_piece(row, c) is None):
                return False
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Pawn:

    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return '_Pawn'

    def can_move(self, board, row, col, row1, col1):
        if col != col1:
            return False

        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        if row + direction == row1:
            return True

        if (row == start_row
                and row + 2 * direction == row1
                and board.field[row + direction][col] is None):
            return True

        return False

    def can_attack(self, board, row, col, row1, col1):
        direction = 1 if (self.color == WHITE) else -1
        return (row + direction == row1
                and (col + 1 == col1 or col - 1 == col1))


class Knight:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return '_Knight'

    def can_move(self, board, row, col, row1, col1):
        if not correct_coords(row1, col1) or not correct_coords(row, col):
            return False
        if board.field[row1][col1] is not None:
            if board.field[row1][col1].get_color == self.color:
                return False
        if row + 2 == row1 and col + 1 == col1:
            return True
        if row + 1 == row1 and col + 2 == col1:
            return True
        if row - 2 == row1 and col + 1 == col1:
            return True
        if row - 1 == row1 and col + 2 == col1:
            return True
        if row + 2 == row1 and col - 1 == col1:
            return True
        if row + 1 == row1 and col - 2 == col1:
            return True
        if row - 2 == row1 and col - 1 == col1:
            return True
        if row - 1 == row1 and col - 2 == col1:
            return True
        return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class King:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return '_King'

    def can_move(self, board, row, col, row1, col1):
        if not correct_coords(row1, col1) or not correct_coords(row, col):
            return False
        if board.field[row1][col1] is not None:
            if board.field[row1][col1].get_color == self.color:
                return False
        if board.is_under_attack(row1, col1, opponent(self.color)):
            return False
        if col == 4 and col1 in [6, 1] and row in [0, 7]:
            return True
        if row + 1 == row1 and col == col1:
            return True
        if row - 1 == row1 and col == col1:
            return True
        if row == row1 and col + 1 == col1:
            return True
        if row == row1 and col - 1 == col1:
            return True
        if row + 1 == row1 and col + 1 == col1:
            return True
        if row + 1 == row1 and col - 1 == col1:
            return True
        if row - 1 == row1 and col + 1 == col1:
            return True
        if row - 1 == row1 and col - 1 == col1:
            return True
        return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Queen:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return '_Queen'

    def can_move(self, board, row, col, row1, col1):
        ch = 'w' if self.color == WHITE else 'b'
        if row1 == row and col1 == col:
            return False
        if board.get_piece(row1, col1) is not None:
            if board.cell(row1, col1)[0] == ch:
                return False
        step_row = 1 if (row1 >= row) else -1
        step_col = 1 if (col1 >= col) else -1
        if row == row1 or col == col1:
            for r in range(row + step_row, row1, step_row):
                if not (board.get_piece(r, col) is None):
                    return False

            for c in range(col + step_col, col1, step_col):
                if not (board.get_piece(row, c) is None):
                    return False
            return True
        else:
            flag = 0
            for i in range(1, 8):
                if row + i * step_row == row1 and col + i * step_col == col1:
                    flag = 1
                    break
            if flag == 0:
                return False
            r = row + step_row
            for c in range(col + step_col, col1, step_col):
                if not (board.get_piece(r, c) is None):
                    return False
                r += step_row
            return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Bishop:

    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return '_Bishop'

    def can_move(self, board, row, col, row1, col1):
        ch = 'w' if self.color == WHITE else 'b'
        if row1 == row and col1 == col:
            return False
        if board.get_piece(row1, col1) is not None:
            if board.cell(row1, col1)[0] == ch:
                return False
        step_row = 1 if (row1 >= row) else -1
        step_col = 1 if (col1 >= col) else -1
        flag = 0
        for i in range(1, 8):
            if row + i * step_row == row1 and col + i * step_col == col1:
                flag = 1
                break
        if flag == 0:
            return False
        r = row + step_row
        for c in range(col + step_col, col1, step_col):
            if not (board.get_piece(r, c) is None):
                return False
            r += step_row
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)