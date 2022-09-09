import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import chess
import time
import sys
import ast
import random
from threading import Thread
from playsound import playsound
from openings import *


if __name__ == '__main__':
    SQUARE_HEIGHT = 85
    SQUARE_WIDTH = 85
    START_MIKE = 'graphics/chess_mike_coach.png'
    HAPPY_MIKE = 'graphics/chess_mike_happy.png'
    SAD_MIKE = 'graphics/chess_mike_sad.png'
    MOVE_SOUND = 'chess_move_sound.mp3'
    WRONG_MOVE_MSG = "That's a wrong move!\nCoach Mike is disappointed at you.\nTry again!"
    THE_END_MSG = "Congrats! Coach Mike is very happy with you.\n Go play some chess!"

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
    try:
        pieces_graphics = sys.argv[2]
    except IndexError:
        pieces_graphics = 1

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

    # Opening information
    try:
        opening_played = OPENING_NUMBERS[ast.literal_eval(sys.argv[1])]
    except IndexError:
        opening_played = QUEENS_GAMBIT
    opening_name = opening_played['name']
    variation_name = random.choice(list(opening_played['variations'].keys()))
    if opening_played['user_plays_white'] == '':
        user_plays_white = random.choice((True, False))
    else:
        user_plays_white = opening_played['user_plays_white']
    max_move_number = len(opening_played['variations'][variation_name])
    moves_to_play = opening_played['variations'][variation_name]




    def draw_board(user_plays_white):
        """ Needed to initiate the board by placing the buttons (squares) on the grids """
        if user_plays_white:
            square = 0
            for row in range(8):
                for column in range(8):
                    list(starting_board.values())[square][0].grid(row=row, column=column+1)
                    square += 1
        else:
            square = 63
            for row in range(8):
                for column in range(8):
                    list(starting_board.values())[square][0].grid(row=row, column=column+1)
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
        sound_thread = Thread(target=lambda: playsound(MOVE_SOUND))
        sound_thread.start()
        time.sleep(0.25)
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
        if move in engine_board.legal_moves:
            return True
        return False


    def move_abstract_piece(start_square, end_square):
        """ Proceeds with the move on abstract the board """
        global move_number
        start_square = chess.parse_square(start_square)
        end_square = chess.parse_square(end_square)
        move = chess.Move(start_square, end_square)
        engine_board.push(move)
        move_number += 1


    def is_end_of_game():
        global GAME_ON
        if move_number > max_move_number - 1:
            time.sleep(0.5)
            messagebox.showwarning(title="You've made it", message=THE_END_MSG)
            GAME_ON = False


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


    def piece_at(square, board):
        """ Tells what kind of piece is on the given square"""
        square = chess.parse_square(square)
        fen = board.board_fen()
        local_board = chess.BaseBoard(fen)
        try:
            return piece_string_to_variable[str(local_board.piece_at(square))]
        except KeyError:
            pass


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

    def show_next_move():
        messagebox.showwarning(title="The next correct move is...", message=moves_to_play[move_number])

    # Window
    window = tk.Tk()
    window.title("board")
    window.config(pady=5, padx=5, bg="#3e3e42")

    # Further window configuration
    opening_name_display = tk.Label(text=opening_name, padx=5, font='Helvetica')
    opening_name_display.grid(row=0, column=9, padx=5, columnspan=2)
    opening_variation_display = tk.Label(text=variation_name, padx=5, font='Helvetica')
    opening_variation_display.grid(row=1, column=9, padx=5)

    # Coach mike display
    img_coach_mike = ImageTk.PhotoImage(Image.open(START_MIKE))
    coach_mike_display = tk.Label(window, image=img_coach_mike)
    coach_mike_display.photo = tk.PhotoImage(file=START_MIKE)
    coach_mike_display.grid(row=2, column=9, padx=5, rowspan=3)

    exit_button = tk.Button(window, text="exit", command=window.destroy)
    exit_button.grid(row=6, column=9, padx=5)

    next_move_button = tk.Button(window, text="Coach Mike please help me!", command=show_next_move)
    next_move_button.grid(row=5, column=9, padx=5)

    if user_plays_white:
        la = tk.Label(window, text='a', fg='white', bg="#3e3e42", font=("Arial", 20))
        la.grid(row=9, column=1)
        lb = tk.Label(window, text='b', fg='white', bg="#3e3e42", font=("Arial", 20))
        lb.grid(row=9, column=2)
        lc = tk.Label(window, text='c', fg='white', bg="#3e3e42", font=("Arial", 20))
        lc.grid(row=9, column=3)
        ld = tk.Label(window, text='d', fg='white', bg="#3e3e42", font=("Arial", 20))
        ld.grid(row=9, column=4)
        le = tk.Label(window, text='e', fg='white', bg="#3e3e42", font=("Arial", 20))
        le.grid(row=9, column=5)
        lf = tk.Label(window, text='f', fg='white', bg="#3e3e42", font=("Arial", 20))
        lf.grid(row=9, column=6)
        lg = tk.Label(window, text='g', fg='white', bg="#3e3e42", font=("Arial", 20))
        lg.grid(row=9, column=7)
        lh = tk.Label(window, text='h', fg='white', bg="#3e3e42", font=("Arial", 20))
        lh.grid(row=9, column=8)
        n8 = tk.Label(window, text='8', fg='white', bg="#3e3e42", font=("Arial", 20))
        n8.grid(row=0, column=0)
        n7 = tk.Label(window, text='7', fg='white', bg="#3e3e42", font=("Arial", 20))
        n7.grid(row=1, column=0)
        n6 = tk.Label(window, text='6', fg='white', bg="#3e3e42", font=("Arial", 20))
        n6.grid(row=2, column=0)
        n5 = tk.Label(window, text='5', fg='white', bg="#3e3e42", font=("Arial", 20))
        n5.grid(row=3, column=0)
        n4 = tk.Label(window, text='4', fg='white', bg="#3e3e42", font=("Arial", 20))
        n4.grid(row=4, column=0)
        n3 = tk.Label(window, text='3', fg='white', bg="#3e3e42", font=("Arial", 20))
        n3.grid(row=5, column=0)
        n2 = tk.Label(window, text='2', fg='white', bg="#3e3e42", font=("Arial", 20))
        n2.grid(row=6, column=0)
        n1 = tk.Label(window, text='1', fg='white', bg="#3e3e42", font=("Arial", 20))
        n1.grid(row=7, column=0)
    else:
        la = tk.Label(window, text='h', fg='white', bg="#3e3e42", font=("Arial", 20))
        la.grid(row=9, column=1)
        lb = tk.Label(window, text='g', fg='white', bg="#3e3e42", font=("Arial", 20))
        lb.grid(row=9, column=2)
        lc = tk.Label(window, text='f', fg='white', bg="#3e3e42", font=("Arial", 20))
        lc.grid(row=9, column=3)
        ld = tk.Label(window, text='e', fg='white', bg="#3e3e42", font=("Arial", 20))
        ld.grid(row=9, column=4)
        le = tk.Label(window, text='d', fg='white', bg="#3e3e42", font=("Arial", 20))
        le.grid(row=9, column=5)
        lf = tk.Label(window, text='c', fg='white', bg="#3e3e42", font=("Arial", 20))
        lf.grid(row=9, column=6)
        lg = tk.Label(window, text='b', fg='white', bg="#3e3e42", font=("Arial", 20))
        lg.grid(row=9, column=7)
        lh = tk.Label(window, text='a', fg='white', bg="#3e3e42", font=("Arial", 20))
        lh.grid(row=9, column=8)
        n8 = tk.Label(window, text='1', fg='white', bg="#3e3e42", font=("Arial", 20))
        n8.grid(row=0, column=0)
        n7 = tk.Label(window, text='2', fg='white', bg="#3e3e42", font=("Arial", 20))
        n7.grid(row=1, column=0)
        n6 = tk.Label(window, text='3', fg='white', bg="#3e3e42", font=("Arial", 20))
        n6.grid(row=2, column=0)
        n5 = tk.Label(window, text='4', fg='white', bg="#3e3e42", font=("Arial", 20))
        n5.grid(row=3, column=0)
        n4 = tk.Label(window, text='5', fg='white', bg="#3e3e42", font=("Arial", 20))
        n4.grid(row=4, column=0)
        n3 = tk.Label(window, text='6', fg='white', bg="#3e3e42", font=("Arial", 20))
        n3.grid(row=5, column=0)
        n2 = tk.Label(window, text='7', fg='white', bg="#3e3e42", font=("Arial", 20))
        n2.grid(row=6, column=0)
        n1 = tk.Label(window, text='8', fg='white', bg="#3e3e42", font=("Arial", 20))
        n1.grid(row=7, column=0)

    figures = {
        p: tk.PhotoImage(file='graphics/graphics{num}/pawn_b.png'.format(num=pieces_graphics)),
        r: tk.PhotoImage(file='graphics/graphics{num}/rook_b.png'.format(num=pieces_graphics)),
        n: tk.PhotoImage(file='graphics/graphics{num}/knight_b.png'.format(num=pieces_graphics)),
        b: tk.PhotoImage(file='graphics/graphics{num}/bishop_b.png'.format(num=pieces_graphics)),
        q: tk.PhotoImage(file='graphics/graphics{num}/queen_b.png'.format(num=pieces_graphics)),
        k: tk.PhotoImage(file='graphics/graphics{num}/king_b.png'.format(num=pieces_graphics)),
        EMPTY: tk.PhotoImage(width=1, height=1),
        P: tk.PhotoImage(file='graphics/graphics{num}/pawn_w.png'.format(num=pieces_graphics)),
        R: tk.PhotoImage(file='graphics/graphics{num}/rook_w.png'.format(num=pieces_graphics)),
        N: tk.PhotoImage(file='graphics/graphics{num}/knight_w.png'.format(num=pieces_graphics)),
        B: tk.PhotoImage(file='graphics/graphics{num}/bishop_w.png'.format(num=pieces_graphics)),
        Q: tk.PhotoImage(file='graphics/graphics{num}/queen_w.png'.format(num=pieces_graphics)),
        K: tk.PhotoImage(file='graphics/graphics{num}/king_w.png'.format(num=pieces_graphics)),
    }

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

    engine_board = chess.Board()
    color_board(starting_board)
    draw_board(user_plays_white)
    game_board = starting_board.copy()

    while GAME_ON:
        is_end_of_game()
        if user_plays_white and move_number % 2 != 0:
            time.sleep(1)
            computer_piece_to_move = piece_at(moves_to_play[move_number][:2], engine_board)
            move_piece(moves_to_play[move_number][:2], moves_to_play[move_number][2:], computer_piece_to_move, game_board)
            move_abstract_piece(moves_to_play[move_number][:2], moves_to_play[move_number][2:])
            squares_clicked = 0

        if not user_plays_white and move_number % 2 == 0:
            time.sleep(1)
            computer_piece_to_move = piece_at(moves_to_play[move_number][:2], engine_board)
            move_piece(moves_to_play[move_number][:2], moves_to_play[move_number][2:], computer_piece_to_move, game_board)
            move_abstract_piece(moves_to_play[move_number][:2], moves_to_play[move_number][2:])
            squares_clicked = 0

        if squares_clicked == 2 and piece_to_move:

            if is_valid_move(start_square, end_square):

                if is_correct_move(moves_to_play, start_square, end_square):
                    move_abstract_piece(start_square, end_square)
                    change_mike(HAPPY_MIKE)
                else:
                    change_mike(SAD_MIKE)
                    messagebox.showerror(title="Wrong move!", message=WRONG_MOVE_MSG)
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