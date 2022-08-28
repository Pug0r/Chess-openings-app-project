import PySimpleGUI as sg

sg.theme('LightGreen')

# dobrze miec stale zapisane w ten sposob
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

# to jest moj pomysl na szachownice, ale na razie nie dziala xd wiec mozna zignorowac chyba
# mam maly problem z tym sposobem tworzenia szachownicy, bo nie wiem jak sie dostac do konkretnego pola
dict_board = {'a1': sg.Button(size=(4, 3)),
              'b1': sg.Button(size=(4, 3)),
              'c1': sg.Button(size=(4, 3)),
              'd1': sg.Button(size=(4, 3)),
              'e1': sg.Button(size=(4, 3)),
              'f1': sg.Button(size=(4, 3)),
              'g1': sg.Button(size=(4, 3)),
              'h1': sg.Button(size=(4, 3)),
              }

# kolorowanie pol szachownicy
def color(i, j):
    if (i + j) % 2 == 0:
        return ('#f0f7f2', '#d3e3d7')
    else:
        return ('#87918a', '#68706a')


board = [[sg.Button(size=(4, 3), key=(i, j), pad=(0, 0), button_color=color(i, j)) for j in range(8)] for i in range(8)]
# na razie nie dziala xd
# board = [list(dict_board.values()) for i in range(8)]
info = [[sg.Text('name')],
        [sg.Text('variation')]]

layout = [[sg.Column(board, element_justification='c'), sg.Column(info, element_justification='c')],
          [sg.Text('czy to dziala')]]

window = sg.Window('chess', layout)

# figurki czarne
# tutaj wydaje sie ze dictionary bedzie pasowal idealnie
# pawn, rook, bishop, knight, queen, king - pionek, wieza...

figures = {PAWN_B:   sg.Image('pionek_b.png'),
           ROOK_B:   sg.Image('wieza_b.png'),
           KNIGHT_B: sg.Image('kon_b.png'),
           BISHOP_B: sg.Image('goniec_b.png'),
           QUEEN_B:  sg.Image('hetman_b.png'),
           KING_B:   sg.Image('krol_b.png')
           }



while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break
