import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import chess
import time
import json

# from menu import GRAPHICS_NO <--- tu cos sie psuje, nie rozumiem do konca czemu ale jak to zrobie to odpala sie menu zamist tablicy szachowej??
SQUARE_HEIGHT = 85
SQUARE_WIDTH = 85
START_MIKE = 'graphics/chess_mike_coach2.png'
HAPPY_MIKE = 'graphics/chess_mike_happy.png'
SAD_MIKE = 'graphics/chess_mike_sad.png'

# Pieces
EMPTY = 0
p = 1
n = 2
b = 3
r = 4
k = 5
q = 6
P = 7
N = 8
B = 9
R = 10
K = 11
Q = 12

piece_string_to_variable = {'p': p,
                            'n': n,
                            'b': b,
                            'r': r,
                            'k': k,
                            'q': q,
                            'P': P,
                            'N': N,
                            'B': B,
                            'R': R,
                            'K': K,
                            'Q': Q}
GAME_ON = True

# I have a very convincing explanation for the use of these global variables!!
# Movement
squares_clicked = 0
start_square = 0
end_square = 0
piece_to_move = 0
move_number = 0
user_plays_white = True

# Near-board information
opening_name = "Queen's Gambit"
variation_name = "Main line"

# Window
window = tk.Tk()
window.title("board")
window.config(pady=20, padx=20, bg="#3e3e42")


def draw_board(user_plays_white):
    """ Needed to initiate the board by placing the buttons (squares) on the grids """
    if user_plays_white:
        square = 0
        for row in range(8):
            for column in range(8):
                list(starting_board.values())[square][0].grid(row=row, column=column)
                square += 1
    else:
        square = 63
        for row in range(8):
            for column in range(8):
                list(starting_board.values())[square][0].grid(row=row, column=column)
                square -= 1


def color_board(board):
    """ Just to avoid configuring color by hand - the dictionary is massive already """
    square = 0
    for row in range(8):
        for column in range(8):
            if (column + row) % 2 == 0:
                list(board.values())[square][0].configure(bg='#eeeed2')
                square += 1
            else:
                list(board.values())[square][0].configure(bg='#769656')
                square += 1


def move_piece(from_square, to_square, piece, board):
    """ Careful, as this function DOES NOT validate the moves"""
    global squares_clicked
    squares_clicked -= 2
    board[from_square][0].configure(image=figures[EMPTY])
    board[from_square][1] = EMPTY
    board[to_square][0].configure(image=figures[piece])
    board[to_square][1] = piece


def is_valid_move(start_square, end_square):
    """ Validates the move that player wants to make  """
    start_square = chess.parse_square(start_square)
    end_square = chess.parse_square(end_square)
    move = chess.Move(start_square, end_square)
    if move in board.legal_moves:
        return True
    return False


def move_abstract_piece(start_square, end_square):
    """ Proceeds with the move on abstract the board """
    global move_number
    start_square = chess.parse_square(start_square)
    end_square = chess.parse_square(end_square)
    move = chess.Move(start_square, end_square)
    board.push(move)
    move_number += 1
    print(board)

def is_correct_move(opening, start_square, end_square):
    """ Ensures the move is valid within chosen opening """
    start_square = chess.parse_square(start_square)
    end_square = chess.parse_square(end_square)
    move = str(chess.Move(start_square, end_square))
    if move in opening[move_number]:
        return True
    else:

        return False


def change_mike(mood):
    """ Changes the photo of Mike on the right of the board"""
    img = ImageTk.PhotoImage(Image.open(mood))
    coach_mike_display.configure(image=img)
    coach_mike_display.image = img


figures = {
    p: tk.PhotoImage(file='graphics/graphics1/pawn_b.png'),
    r: tk.PhotoImage(file='graphics/graphics1/rook_b.png'),
    n: tk.PhotoImage(file='graphics/graphics1/knight_b.png'),
    b: tk.PhotoImage(file='graphics/graphics1/bishop_b.png'),
    q: tk.PhotoImage(file='graphics/graphics1/queen_b.png'),
    k: tk.PhotoImage(file='graphics/graphics1/king_b.png'),
    EMPTY: tk.PhotoImage(width=1, height=1),
    P: tk.PhotoImage(file='graphics/graphics1/pawn_w.png'),
    R: tk.PhotoImage(file='graphics/graphics1/rook_w.png'),
    N: tk.PhotoImage(file='graphics/graphics1/knight_w.png'),
    B: tk.PhotoImage(file='graphics/graphics1/bishop_w.png'),
    Q: tk.PhotoImage(file='graphics/graphics1/queen_w.png'),
    K: tk.PhotoImage(file='graphics/graphics1/king_w.png'),
}


def piece_at(square, board):
    """ Tells what kind of piece is on the given square"""
    square = chess.parse_square(square)
    fen = board.board_fen()
    local_board = chess.BaseBoard(fen)
    return piece_string_to_variable[str(local_board.piece_at(square))]


def square_info(row, column):
    """ Returns info from the square pressed and puts it into global variables """
    global squares_clicked, start_square, end_square, piece_to_move
    if not squares_clicked:
        start_square = row + column
        piece_to_move = starting_board[row + column][1]
        squares_clicked += 1
    else:
        end_square = row + column
        squares_clicked += 1
    # to be deleted, development purposes
    print(row + column, piece_to_move)
    print(squares_clicked)


def wrong_move_display():
    # global GAME_ON
    # GAME_ON = False
    messagebox.showerror(title="Wrong move!", message="That's a wrong move!\nCoach Mike is disappointed at you.\nTry "
                                                      "again!")



starting_board = {
    'a8': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[r],
                     command=lambda row='a', column='8': square_info(row, column)), r],
    'b8': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[n],
                     command=lambda row='b', column='8': square_info(row, column)), n],
    'c8': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[b],
                     command=lambda row='c', column='8': square_info(row, column)), b],
    'd8': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[q],
                     command=lambda row='d', column='8': square_info(row, column)), q],
    'e8': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[k],
                     command=lambda row='e', column='8': square_info(row, column)), k],
    'f8': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[b],
                     command=lambda row='f', column='8': square_info(row, column)), b],
    'g8': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[n],
                     command=lambda row='g', column='8': square_info(row, column)), n],
    'h8': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[r],
                     command=lambda row='h', column='8': square_info(row, column)), r],
    'a7': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[p],
                     command=lambda row='a', column='7': square_info(row, column)), p],
    'b7': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[p],
                     command=lambda row='b', column='7': square_info(row, column)), p],
    'c7': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[p],
                     command=lambda row='c', column='7': square_info(row, column)), p],
    'd7': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[p],
                     command=lambda row='d', column='7': square_info(row, column)), p],
    'e7': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[p],
                     command=lambda row='e', column='7': square_info(row, column)), p],
    'f7': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[p],
                     command=lambda row='f', column='7': square_info(row, column)), p],
    'g7': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[p],
                     command=lambda row='g', column='7': square_info(row, column)), p],
    'h7': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[p],
                     command=lambda row='h', column='7': square_info(row, column)), p],
    'a6': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='a', column='6': square_info(row, column)), EMPTY],
    'b6': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='b', column='6': square_info(row, column)), EMPTY],
    'c6': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='c', column='6': square_info(row, column)), EMPTY],
    'd6': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='d', column='6': square_info(row, column)), EMPTY],
    'e6': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='e', column='6': square_info(row, column)), EMPTY],
    'f6': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='f', column='6': square_info(row, column)), EMPTY],
    'g6': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='g', column='6': square_info(row, column)), EMPTY],
    'h6': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='h', column='6': square_info(row, column)), EMPTY],
    'a5': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='a', column='5': square_info(row, column)), EMPTY],
    'b5': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='b', column='5': square_info(row, column)), EMPTY],
    'c5': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='c', column='5': square_info(row, column)), EMPTY],
    'd5': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='d', column='5': square_info(row, column)), EMPTY],
    'e5': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='e', column='5': square_info(row, column)), EMPTY],
    'f5': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='f', column='5': square_info(row, column)), EMPTY],
    'g5': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='g', column='5': square_info(row, column)), EMPTY],
    'h5': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='h', column='5': square_info(row, column)), EMPTY],
    'a4': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='a', column='4': square_info(row, column)), EMPTY],
    'b4': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='b', column='4': square_info(row, column)), EMPTY],
    'c4': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='c', column='4': square_info(row, column)), EMPTY],
    'd4': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='d', column='4': square_info(row, column)), EMPTY],
    'e4': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='e', column='4': square_info(row, column)), EMPTY],
    'f4': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='f', column='4': square_info(row, column)), EMPTY],
    'g4': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='g', column='4': square_info(row, column)), EMPTY],
    'h4': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='h', column='4': square_info(row, column)), EMPTY],
    'a3': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='a', column='3': square_info(row, column)), EMPTY],
    'b3': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='b', column='3': square_info(row, column)), EMPTY],
    'c3': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='c', column='3': square_info(row, column)), EMPTY],
    'd3': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='d', column='3': square_info(row, column)), EMPTY],
    'e3': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='e', column='3': square_info(row, column)), EMPTY],
    'f3': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='f', column='3': square_info(row, column)), EMPTY],
    'g3': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='g', column='3': square_info(row, column)), EMPTY],
    'h3': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY],
                     command=lambda row='h', column='3': square_info(row, column)), EMPTY],
    'a2': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[P],
                     command=lambda row='a', column='2': square_info(row, column)), P],
    'b2': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[P],
                     command=lambda row='b', column='2': square_info(row, column)), P],
    'c2': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[P],
                     command=lambda row='c', column='2': square_info(row, column)), P],
    'd2': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[P],
                     command=lambda row='d', column='2': square_info(row, column)), P],
    'e2': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[P],
                     command=lambda row='e', column='2': square_info(row, column)), P],
    'f2': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[P],
                     command=lambda row='f', column='2': square_info(row, column)), P],
    'g2': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[P],
                     command=lambda row='g', column='2': square_info(row, column)), P],
    'h2': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[P],
                     command=lambda row='h', column='2': square_info(row, column)), P],
    'a1': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[R],
                     command=lambda row='a', column='1': square_info(row, column)), R],
    'b1': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[N],
                     command=lambda row='b', column='1': square_info(row, column)), N],
    'c1': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[B],
                     command=lambda row='c', column='1': square_info(row, column)), B],
    'd1': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[Q],
                     command=lambda row='d', column='1': square_info(row, column)), Q],
    'e1': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[K],
                     command=lambda row='e', column='1': square_info(row, column)), K],
    'f1': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[B],
                     command=lambda row='f', column='1': square_info(row, column)), B],
    'g1': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[N],
                     command=lambda row='g', column='1': square_info(row, column)), N],
    'h1': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[R],
                     command=lambda row='h', column='1': square_info(row, column)), R],
}

# Further window configuration
opening_name_display = tk.Label(text=opening_name, padx=10, font='Helvetica')
opening_name_display.grid(row=0, column=9, padx=10, columnspan=2)
opening_variation_display = tk.Label(text=variation_name, padx=10, font='Helvetica')
opening_variation_display.grid(row=1, column=9, padx=10)

# Coach mike display
img_coach_mike = ImageTk.PhotoImage(Image.open(START_MIKE))
coach_mike_display = tk.Label(window, image=img_coach_mike)
coach_mike_display.photo = tk.PhotoImage(file=START_MIKE)
coach_mike_display.grid(row=2, column=9, padx=10, rowspan=3)

exit_button = tk.Button(window, text="exit", command=window.destroy)
exit_button.grid(row=6, column=9, padx=10)

queens_gambit = {0: ('d2d4'), 1: ('d7d5'), 2: ('c2c4'), 3: ('d5c4')}
board = chess.Board()
color_board(starting_board)
draw_board(user_plays_white)
game_board = starting_board.copy()

while GAME_ON:
    if user_plays_white and move_number % 2 != 0:
        time.sleep(1)
        computer_piece_to_move = piece_at(queens_gambit[move_number][:2], board)
        move_piece(queens_gambit[move_number][:2], queens_gambit[move_number][2:], computer_piece_to_move, game_board)
        move_abstract_piece(queens_gambit[move_number][:2], queens_gambit[move_number][2:])
        squares_clicked = 0

    if squares_clicked == 2 and piece_to_move:

        if is_valid_move(start_square, end_square):

            if is_correct_move(queens_gambit, start_square, end_square):
                move_abstract_piece(start_square, end_square)
                change_mike(HAPPY_MIKE)
            else:
                change_mike(SAD_MIKE)
                wrong_move_display()
                squares_clicked = 0
                continue
            move_piece(start_square, end_square, piece_to_move, game_board)

        else:
            squares_clicked = 0

    if not piece_to_move:
        squares_clicked = 0

    window.update()

while True:
    window.update()