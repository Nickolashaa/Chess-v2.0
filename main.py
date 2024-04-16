import pygame
from Cartoons.Sprites import *
from Board import Board

def main():
    pygame.init()
    time = pygame.time.Clock()
    screen = pygame.display.set_mode((640, 640))
    all_sprites = pygame.sprite.Group()


    row, col, row1, col1 = None, None, None, None
    board = Board()
    a1 = A1()
    a2 = A2()
    a3 = A3()
    a4 = A4()
    a5 = A5()
    a6 = A6()
    a7 = A7()
    a8 = A8()
    b1 = B1()
    b2 = B2()
    b3 = B3()
    b4 = B4()
    b5 = B5()
    b6 = B6()
    b7 = B7()
    b8 = B8()
    c1 = C1()
    c2 = C2()
    c3 = C3()
    c4 = C4()
    c5 = C5()
    c6 = C6()
    c7 = C7()
    c8 = C8()
    d1 = D1()
    d2 = D2()
    d3 = D3()
    d4 = D4()
    d5 = D5()
    d6 = D6()
    d7 = D7()
    d8 = D8()
    e1 = E1()
    e2 = E2()
    e3 = E3()
    e4 = E4()
    e5 = E5()
    e6 = E6()
    e7 = E7()
    e8 = E8()
    f1 = F1()
    f2 = F2()
    f3 = F3()
    f4 = F4()
    f5 = F5()
    f6 = F6()
    f7 = F7()
    f8 = F8()
    g1 = G1()
    g2 = G2()
    g3 = G3()
    g4 = G4()
    g5 = G5()
    g6 = G6()
    g7 = G7()
    g8 = G8()
    h1 = H1()
    h2 = H2()
    h3 = H3()
    h4 = H4()
    h5 = H5()
    h6 = H6()
    h7 = H7()
    h8 = H8()


    all_sprites.add(a1, a2, a3, a4, a5, a6, a7, a8,
                    b1, b2, b3, b4, b5, b6, b7, b8,
                    c1, c2, c3, c4, c5, c6, c7, c8,
                    d1, d2, d3, d4, d5, d6, d7, d8,
                    e1, e2, e3, e4, e5, e6, e7, e8,
                    g1, g2, g3, g4, g5, g6, g7, g8,
                    f1, f2, f3, f4, f5, f6, f7, f8,
                    h1, h2, h3, h4, h5, h6, h7, h8)


    a2.key = 'W_Pawn'
    b2.key = 'W_Pawn'
    c2.key = 'W_Pawn'
    d2.key = 'W_Pawn'
    e2.key = 'W_Pawn'
    f2.key = 'W_Pawn'
    g2.key = 'W_Pawn'
    h2.key = 'W_Pawn'
    a7.key = 'B_Pawn'
    b7.key = 'B_Pawn'
    c7.key = 'B_Pawn'
    d7.key = 'B_Pawn'
    e7.key = 'B_Pawn'
    f7.key = 'B_Pawn'
    g7.key = 'B_Pawn'
    h7.key = 'B_Pawn'
    a1.key = 'W_Rook'
    b1.key = 'W_Knight'
    c1.key = 'W_Bishop'
    d1.key = 'W_Queen'
    e1.key = 'W_King'
    f1.key = 'W_Bishop'
    g1.key = 'W_Knight'
    h1.key = 'W_Rook'
    a8.key = 'B_Rook'
    b8.key = 'B_Knight'
    c8.key = 'B_Bishop'
    d8.key = 'B_Queen'
    e8.key = 'B_King'
    f8.key = 'B_Bishop'
    g8.key = 'B_Knight'
    h8.key = 'B_Rook'
    all_sprites.update()

    game = True

    while game:
        all_sprites.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for sprite in all_sprites.sprites():
                        if sprite.rect.collidepoint(event.pos):
                            print(sprite.name)
                            print(sprite.key)
                            print(sprite.cord)
                            if row is None and col is None:
                                row, col = sprite.cord
                            else:
                                row1, col1 = sprite.cord
                                if board.move_piece(row, col, row1, col1):
                                    for i in range(len(board.field)):
                                        for j in range(len(board.field[i])):
                                            if board.field[i][j] is None:
                                                for sprite1 in all_sprites.sprites():
                                                    if sprite1.cord == (i, j):
                                                        sprite1.key = 'Default'
                                                        pygame.display.update()
                                                        break
                                            else:
                                                for sprite1 in all_sprites.sprites():
                                                    if sprite1.cord == (i, j):
                                                        sprite1.key = board.cell(i, j)
                                                        all_sprites.update()
                                                        pygame.display.update()
                                                        break
                                    row, col, row1, col1 = None, None, None, None
                                else:
                                    print(False)
                                    row, col, row1, col1 = None, None, None, None
                            break
        all_sprites.update()
        pygame.display.update()
        time.tick(20)


if __name__ == '__main__':
    main()
