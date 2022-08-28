# to tylko dla testu, chce sprawdzic czy w Tkinter da to sie zrobic sensowniej (chodzi mi tylko o szachownice, reszte bedzie chyba
# latwiej w pysimplegui
from tkinter import *

SQUARE_HEIGHT = 4
SQUARE_WIDTH = 10


def color_board(board):
    square = 0
    for column in range(8):
        for row in range(8):
            if (column + row) % 2 == 0:
                list(dict_board.values())[square].configure(bg='#769656')
                square += 1
            else:
                list(dict_board.values())[square].configure(bg='#eeeed2')
                square += 1

# Window
window = Tk()
window.title("board")
window.config(pady=10, padx=10, bg="#607EAA")

rook_img = PhotoImage(file='wieza_b.png')

dict_board = {'a8': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'b8': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'c8': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'd8': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'e8': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'f8': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'g8': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'h8': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH),
              'a7': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'b7': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'c7': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'd7': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'e7': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'f7': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'g7': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'h7': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH),
              'a6': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'b6': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'c6': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'd6': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'e6': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'f6': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'g6': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'h6': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH),
              'a5': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'b5': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'c5': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'd5': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'e5': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'f5': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'g5': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'h5': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH),
              'a4': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'b4': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'c4': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'd4': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'e4': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'f4': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'g4': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'h4': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH),
              'a3': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=rook_img), 'b3': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'c3': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'd3': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'e3': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'f3': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'g3': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'h3': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH),
              'a2': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=rook_img), 'b2': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'c2': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'd2': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'e2': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'f2': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'g2': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'h2': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH),
              'a1': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH, image=rook_img), 'b1': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'c1': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'd1': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'e1': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'f1': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'g1': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH), 'h1': Button(window, height=SQUARE_HEIGHT, width=SQUARE_WIDTH),
              }

color_board(dict_board)
# zastanow sie czy lepiej grid czy frame?
square = 0
for column in range(8):
    for row in range(8):
        list(dict_board.values())[square].grid(row=row, column=column)
        square += 1

window.mainloop()
