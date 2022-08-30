import tkinter as tk
from move_validation import is_valid_move


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

GAME_ON = True

# I have a very convincing explanation for the use of these global variables!!
# Movement
squares_clicked = 0
start_square = 0
end_square = 0
piece_to_move = 0


# Near-board information
opening_name = "Queen's Gambit"
variation_name = "Main line"
coach_mike = 'chess_mike_coach.png'

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


figures = {
           PAWN_B:  tk.PhotoImage(file='graphics/pawn_b.png'),
           ROOK_B:  tk.PhotoImage(file='graphics/rook_b.png'),
           KNIGHT_B:  tk.PhotoImage(file='graphics/knight_b.png'),
           BISHOP_B:  tk.PhotoImage(file='graphics/bishop_b.png'),
           QUEEN_B:  tk.PhotoImage(file='graphics/queen_b.png'),
           KING_B:  tk.PhotoImage(file='graphics/king_b.png'),
           EMPTY:  tk.PhotoImage(width=1, height=1),
           PAWN_W:  tk.PhotoImage(file='graphics/pawn_w.png'),
           ROOK_W:  tk.PhotoImage(file='graphics/rook_w.png'),
           KNIGHT_W:  tk.PhotoImage(file='graphics/knight_w.png'),
           BISHOP_W:  tk.PhotoImage(file='graphics/bishop_w.png'),
           QUEEN_W:  tk.PhotoImage(file='graphics/queen_w.png'),
           KING_W:  tk.PhotoImage(file='graphics/king_w.png'),
           }


def square_info(row, column):
    """ Returns info from the square pressed and puts it into global variables """
    global squares_clicked, start_square, end_square, piece_to_move
    if not squares_clicked:
        start_square = row+column
        piece_to_move = starting_board[row + column][1]
        squares_clicked += 1
    else:
        end_square = row+column
        squares_clicked += 1
    # to be deleted, development purposes
    print(row+column, piece_to_move)
    print(squares_clicked)


starting_board = {
                  'a8': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[ROOK_B], command=lambda row='a', column='8': square_info(row, column)), ROOK_B],
                  'b8': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[KNIGHT_B], command=lambda row='b', column='8': square_info(row, column)), KNIGHT_B],
                  'c8': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[BISHOP_B], command=lambda row='c', column='8': square_info(row, column)), BISHOP_B],
                  'd8': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[QUEEN_B], command=lambda row='d', column='8': square_info(row, column)), QUEEN_B],
                  'e8': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[KING_B], command=lambda row='e', column='8': square_info(row, column)), KING_B],
                  'f8': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[BISHOP_B], command=lambda row='f', column='8': square_info(row, column)), BISHOP_B],
                  'g8': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[KNIGHT_B], command=lambda row='g', column='8': square_info(row, column)), KNIGHT_B],
                  'h8': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[ROOK_B], command=lambda row='h', column='8': square_info(row, column)), ROOK_B],
                  'a7': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_B], command=lambda row='a', column='7': square_info(row, column)), PAWN_B],
                  'b7': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_B], command=lambda row='b', column='7': square_info(row, column)), PAWN_B],
                  'c7': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_B], command=lambda row='c', column='7': square_info(row, column)), PAWN_B],
                  'd7': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_B], command=lambda row='d', column='7': square_info(row, column)), PAWN_B],
                  'e7': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_B], command=lambda row='e', column='7': square_info(row, column)), PAWN_B],
                  'f7': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_B], command=lambda row='f', column='7': square_info(row, column)), PAWN_B],
                  'g7': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_B], command=lambda row='g', column='7': square_info(row, column)), PAWN_B],
                  'h7': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_B], command=lambda row='h', column='7': square_info(row, column)), PAWN_B],
                  'a6': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='a', column='6': square_info(row, column)), EMPTY],
                  'b6': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='b', column='6': square_info(row, column)), EMPTY],
                  'c6': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='c', column='6': square_info(row, column)), EMPTY],
                  'd6': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='d', column='6': square_info(row, column)), EMPTY],
                  'e6': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='e', column='6': square_info(row, column)), EMPTY],
                  'f6': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='f', column='6': square_info(row, column)), EMPTY],
                  'g6': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='g', column='6': square_info(row, column)), EMPTY],
                  'h6': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='h', column='6': square_info(row, column)), EMPTY],
                  'a5': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='a', column='5': square_info(row, column)), EMPTY],
                  'b5': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='b', column='5': square_info(row, column)), EMPTY],
                  'c5': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='c', column='5': square_info(row, column)), EMPTY],
                  'd5': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='d', column='5': square_info(row, column)), EMPTY],
                  'e5': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='e', column='5': square_info(row, column)), EMPTY],
                  'f5': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='f', column='5': square_info(row, column)), EMPTY],
                  'g5': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='g', column='5': square_info(row, column)), EMPTY],
                  'h5': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='h', column='5': square_info(row, column)), EMPTY],
                  'a4': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='a', column='4': square_info(row, column)), EMPTY],
                  'b4': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='b', column='4': square_info(row, column)), EMPTY],
                  'c4': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='c', column='4': square_info(row, column)), EMPTY],
                  'd4': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='d', column='4': square_info(row, column)), EMPTY],
                  'e4': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='e', column='4': square_info(row, column)), EMPTY],
                  'f4': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='f', column='4': square_info(row, column)), EMPTY],
                  'g4': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='g', column='4': square_info(row, column)), EMPTY],
                  'h4': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='h', column='4': square_info(row, column)), EMPTY],
                  'a3': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='a', column='3': square_info(row, column)), EMPTY],
                  'b3': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='b', column='3': square_info(row, column)), EMPTY],
                  'c3': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='c', column='3': square_info(row, column)), EMPTY],
                  'd3': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='d', column='3': square_info(row, column)), EMPTY],
                  'e3': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='e', column='3': square_info(row, column)), EMPTY],
                  'f3': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='f', column='3': square_info(row, column)), EMPTY],
                  'g3': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='g', column='3': square_info(row, column)), EMPTY],
                  'h3': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[EMPTY], command=lambda row='h', column='3': square_info(row, column)), EMPTY],
                  'a2': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_W], command=lambda row='a', column='2': square_info(row, column)), PAWN_W],
                  'b2': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_W], command=lambda row='b', column='2': square_info(row, column)), PAWN_W],
                  'c2': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_W], command=lambda row='c', column='2': square_info(row, column)), PAWN_W],
                  'd2': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_W], command=lambda row='d', column='2': square_info(row, column)), PAWN_W],
                  'e2': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_W], command=lambda row='e', column='2': square_info(row, column)), PAWN_W],
                  'f2': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_W], command=lambda row='f', column='2': square_info(row, column)), PAWN_W],
                  'g2': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_W], command=lambda row='g', column='2': square_info(row, column)), PAWN_W],
                  'h2': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[PAWN_W], command=lambda row='h', column='2': square_info(row, column)), PAWN_W],
                  'a1': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[ROOK_W], command=lambda row='a', column='1': square_info(row, column)), ROOK_W],
                  'b1': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[KNIGHT_W], command=lambda row='b', column='1': square_info(row, column)), KNIGHT_W],
                  'c1': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[BISHOP_W], command=lambda row='c', column='1': square_info(row, column)), BISHOP_W],
                  'd1': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[QUEEN_W], command=lambda row='d', column='1': square_info(row, column)), QUEEN_W],
                  'e1': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[KING_W], command=lambda row='e', column='1': square_info(row, column)), KING_W],
                  'f1': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[BISHOP_W], command=lambda row='f', column='1': square_info(row, column)), BISHOP_W],
                  'g1': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[KNIGHT_W], command=lambda row='g', column='1': square_info(row, column)), KNIGHT_W],
                  'h1': [tk.Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=figures[ROOK_W], command=lambda row='h', column='1': square_info(row, column)), ROOK_W],
                  }

# Further window configuration
opening_name_display = tk.Label(text=opening_name, padx=10, font='Helvetica')
opening_name_display.grid(row=0, column=9, padx=10)
opening_variation_display = tk.Label(text=variation_name, padx=10, font='Helvetica')
opening_variation_display.grid(row=1, column=9, padx=10)
# cos nie dziala, zerknij na to pozniej
# coach_mike_display = tk.Label(image=coach_mike, padx=10)
# coach_mike_display.grid(row=2, column=9, padx=10)
exit_button = tk.Button(window, text="exit")
exit_button.grid(row=6, column=9, padx=10)

color_board(starting_board)
draw_board(1)
game_board = starting_board.copy()
while GAME_ON:
    if squares_clicked == 2 and piece_to_move:
        if is_valid_move(start_square, end_square):
            move_piece(start_square, end_square, piece_to_move, game_board)
        else:
            squares_clicked = 0
    if not piece_to_move:
        squares_clicked = 0

    window.update()


