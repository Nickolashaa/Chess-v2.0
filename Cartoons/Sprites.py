import pygame


WHITE = 1
BLACK = 2

step = 80

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8']


class Square(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Cartoons/B_Default.png")
        self.rect = self.image.get_rect()
        self.name = self.__class__.__name__
        self.cord = (numbers.index(self.name[1]), letters.index(self.name[0]))
        self.key = 'Default'
        self.color = None

    def update(self):
        if self.key == 'B_Pawn':
            if self.color == WHITE:
                self.image = pygame.image.load("Cartoons/W_B_Pawn.png")
            else:
                self.image = pygame.image.load("Cartoons/B_B_Pawn.png")
        if self.key == 'B_Rook':
            if self.color == WHITE:
                self.image = pygame.image.load("Cartoons/W_B_Rook.png")
            else:
                self.image = pygame.image.load("Cartoons/B_B_Rook.png")
        if self.key == 'B_Knight':
            if self.color == WHITE:
                self.image = pygame.image.load("Cartoons/W_B_Knight.png")
            else:
                self.image = pygame.image.load("Cartoons/B_B_Knight.png")
        if self.key == 'B_Bishop':
            if self.color == WHITE:
                self.image = pygame.image.load("Cartoons/W_B_Bishop.png")
            else:
                self.image = pygame.image.load("Cartoons/B_B_Bishop.png")
        if self.key == 'B_Queen':
            if self.color == WHITE:
                self.image = pygame.image.load("Cartoons/W_B_Queen.png")
            else:
                self.image = pygame.image.load("Cartoons/B_B_Queen.png")
        if self.key == 'B_King':
            if self.color == WHITE:
                self.image = pygame.image.load("Cartoons/W_B_King.png")
            else:
                self.image = pygame.image.load("Cartoons/B_B_King.png")
        if self.key == 'W_Pawn':
            if self.color == WHITE:
                self.image = pygame.image.load("Cartoons/W_W_Pawn.png")
            else:
                self.image = pygame.image.load("Cartoons/B_W_Pawn.png")
        if self.key == 'W_Rook':
            if self.color == WHITE:
                self.image = pygame.image.load("Cartoons/W_W_Rook.png")
            else:
                self.image = pygame.image.load("Cartoons/B_W_Rook.png")
        if self.key == 'W_Knight':
            if self.color == WHITE:
                self.image = pygame.image.load("Cartoons/W_W_Knight.png")
            else:
                self.image = pygame.image.load("Cartoons/B_W_Knight.png")
        if self.key == 'W_Bishop':
            if self.color == WHITE:
                self.image = pygame.image.load("Cartoons/W_W_Bishop.png")
            else:
                self.image = pygame.image.load("Cartoons/B_W_Bishop.png")
        if self.key == 'W_Queen':
            if self.color == WHITE:
                self.image = pygame.image.load("Cartoons/W_W_Queen.png")
            else:
                self.image = pygame.image.load("Cartoons/B_W_Queen.png")
        if self.key == 'W_King':
            if self.color == WHITE:
                self.image = pygame.image.load("Cartoons/W_W_King.png")
            else:
                self.image = pygame.image.load("Cartoons/B_W_King.png")
        if self.key == 'Default':
            if self.color == WHITE:
                self.image = pygame.image.load("Cartoons/W_Default.png")
            else:
                self.image = pygame.image.load("Cartoons/B_Default.png")


class A8(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 0
        self.rect.y += step * 0
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class B8(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 1
        self.rect.y += step * 0
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class C8(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 2
        self.rect.y += step * 0
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class D8(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 3
        self.rect.y += step * 0
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class E8(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 4
        self.rect.y += step * 0
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class F8(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 5
        self.rect.y += step * 0
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class G8(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 6
        self.rect.y += step * 0
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class H8(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 7
        self.rect.y += step * 0
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class A7(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 0
        self.rect.y += step * 1
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class B7(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 1
        self.rect.y += step * 1
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class C7(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 2
        self.rect.y += step * 1
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class D7(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 3
        self.rect.y += step * 1
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class E7(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 4
        self.rect.y += step * 1
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class F7(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 5
        self.rect.y += step * 1
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class G7(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 6
        self.rect.y += step * 1
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class H7(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 7
        self.rect.y += step * 1
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class A6(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 0
        self.rect.y += step * 2
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class B6(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 1
        self.rect.y += step * 2
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class C6(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 2
        self.rect.y += step * 2
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class D6(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 3
        self.rect.y += step * 2
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class E6(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 4
        self.rect.y += step * 2
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class F6(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 5
        self.rect.y += step * 2
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class G6(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 6
        self.rect.y += step * 2
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class H6(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 7
        self.rect.y += step * 2
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class A5(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 0
        self.rect.y += step * 3
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class B5(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 1
        self.rect.y += step * 3
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class C5(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 2
        self.rect.y += step * 3
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class D5(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 3
        self.rect.y += step * 3
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class E5(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 4
        self.rect.y += step * 3
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class F5(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 5
        self.rect.y += step * 3
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class G5(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 6
        self.rect.y += step * 3
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class H5(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 7
        self.rect.y += step * 3
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class A4(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 0
        self.rect.y += step * 4
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class B4(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 1
        self.rect.y += step * 4
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class C4(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 2
        self.rect.y += step * 4
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class D4(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 3
        self.rect.y += step * 4
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class E4(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 4
        self.rect.y += step * 4
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class F4(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 5
        self.rect.y += step * 4
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class G4(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 6
        self.rect.y += step * 4
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class H4(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 7
        self.rect.y += step * 4
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class A3(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 0
        self.rect.y += step * 5
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class B3(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 1
        self.rect.y += step * 5
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class C3(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 2
        self.rect.y += step * 5
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class D3(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 3
        self.rect.y += step * 5
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class E3(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 4
        self.rect.y += step * 5
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class F3(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 5
        self.rect.y += step * 5
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class G3(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 6
        self.rect.y += step * 5
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class H3(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 7
        self.rect.y += step * 5
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class A2(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 0
        self.rect.y += step * 6
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class B2(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 1
        self.rect.y += step * 6
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class C2(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 2
        self.rect.y += step * 6
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class D2(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 3
        self.rect.y += step * 6
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class E2(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 4
        self.rect.y += step * 6
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class F2(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 5
        self.rect.y += step * 6
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class G2(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 6
        self.rect.y += step * 6
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class H2(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 7
        self.rect.y += step * 6
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class A1(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 0
        self.rect.y += step * 7
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class B1(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 1
        self.rect.y += step * 7
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class C1(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 2
        self.rect.y += step * 7
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class D1(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 3
        self.rect.y += step * 7
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class E1(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 4
        self.rect.y += step * 7
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class F1(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 5
        self.rect.y += step * 7
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class G1(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 6
        self.rect.y += step * 7
        self.color = BLACK
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")


class H1(Square):
    def __init__(self):
        super().__init__()
        self.rect.x += step * 7
        self.rect.y += step * 7
        self.color = WHITE
        if self.color == WHITE:
            self.image = pygame.image.load("Cartoons/W_Default.png")
        else:
            self.image = pygame.image.load("Cartoons/B_Default.png")