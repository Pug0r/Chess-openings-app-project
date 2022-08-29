import tkinter
from tkinter import *

SQUARE_HEIGHT = 85
SQUARE_WIDTH = 85

EMPTY = 0
PAWN_B = 1
KNIGHT_B = 2
BISHOP_B = 3
ROOK_B = 4
KING_B = 5
QUEEN_B = 6
PAWN_W = 7
KNIGHT_W = 8
BISHOP_W = 9
ROOK_W = 10
KING_W = 11
QUEEN_W = 12

LETTER_TO_NUMBER = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

IMAGE_TO_PIECE = {'pyimage1': PAWN_B, 'pyimage2': ROOK_B, 'pyimage3': KNIGHT_B, 'pyimage4': BISHOP_B,
                  'pyimage5': QUEEN_B, 'pyimage6': KING_B}

# Window
window = Tk()
window.title("board")
window.config(pady=10, padx=10, bg="#607EAA")


def draw_board():
    square = 0
    for row in range(8):
        for column in range(8):
            list(board.values())[square].grid(row=row, column=column)
            square += 1


def color_board(board):
    square = 0
    for row in range(8):
        for column in range(8):
            if (column + row) % 2 == 0:
                list(board.values())[square].configure(bg='#eeeed2')
                square += 1
            else:
                list(board.values())[square].configure(bg='#769656')
                square += 1


figures = {
           PAWN_B: PhotoImage(file='graphics/pawn_b.png'),
           ROOK_B: PhotoImage(file='graphics/rook_b.png'),
           KNIGHT_B: PhotoImage(file='graphics/knight_b.png'),
           BISHOP_B: PhotoImage(file='graphics/bishop_b.png'),
           QUEEN_B: PhotoImage(file='graphics/queen_b.png'),
           KING_B: PhotoImage(file='graphics/king_b.png'),
           EMPTY: tkinter.PhotoImage(width=1, height=1),
           PAWN_W: PhotoImage(file='graphics/pawn_b.png'),
           ROOK_W: PhotoImage(file='graphics/rook_b.png'),
           KNIGHT_W: PhotoImage(file='graphics/knight_b.png'),
           BISHOP_W: PhotoImage(file='graphics/bishop_b.png'),
           QUEEN_W: PhotoImage(file='graphics/queen_b.png'),
           KING_W: PhotoImage(file='graphics/king_b.png'),
           }


def square_info(row, column):
    print(board['b8'].cget('image'))
    print('it works!')
    print(row + column)
    return row + column


board = {'a8': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[ROOK_B],
                      command=lambda row='a', column='8': square_info(row, column)),
         'b8': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[KNIGHT_B]),
         'c8': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[BISHOP_B]),
         'd8': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[KING_B]),
         'e8': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[QUEEN_B]),
         'f8': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[BISHOP_B]),
         'g8': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[KNIGHT_B]),
         'h8': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[ROOK_B]),
         'a7': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_B]),
         'b7': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_B]),
         'c7': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_B]),
         'd7': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_B]),
         'e7': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_B]),
         'f7': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_B]),
         'g7': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_B]),
         'h7': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_B]),
         'a6': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'b6': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'c6': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'd6': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'e6': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'f6': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'g6': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'h6': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'a5': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'b5': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'c5': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'd5': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'e5': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'f5': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'g5': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'h5': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'a4': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'b4': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'c4': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'd4': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'e4': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'f4': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'g4': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'h4': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'a3': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'b3': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'c3': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'd3': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'e3': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'f3': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'g3': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'h3': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY]),
         'a2': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_B]),
         'b2': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_B]),
         'c2': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_B]),
         'd2': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_B]),
         'e2': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_B]),
         'f2': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_B]),
         'g2': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_B]),
         'h2': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_B]),
         'a1': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[ROOK_B]),
         'b1': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[KNIGHT_B]),
         'c1': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[BISHOP_B]),
         'd1': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[KING_B]),
         'e1': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[QUEEN_B]),
         'f1': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[BISHOP_B]),
         'g1': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[KNIGHT_B]),
         'h1': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[ROOK_B]),
         }

color_board(board)
draw_board()

# PROTOTYPE of movement function
def move_piece(start_square, finish_square, board):
    piece = IMAGE_TO_PIECE[board[start_square].cget('image')]
    board[start_square].configure(image=figures[EMPTY])
    print(piece)
    # board[finish_square].configure(image=piece.cget('image'))


move_piece('a1', 'b3', board)
draw_board()

window.mainloop()
