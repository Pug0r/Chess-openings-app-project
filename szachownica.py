import PySimpleGUI as sg

sg.theme('LightGreen')

#kolorowanie pol szachownicy
def color(i, j):
	if (i + j)%2 == 0:
		return ('#f0f7f2', '#d3e3d7')
	else:
		return ('#87918a', '#68706a')

board = [[sg.Button(size=(4,3), key = (i, j), pad = (0,0), button_color = color(i, j)) for j in range(8)] for i in range(8)]


info = [[sg.Text('name')],
		[sg.Text('variation')]]


layout = [[sg.Column(board, element_justification = 'c'), sg.Column(info, element_justification = 'c')],
		[sg.Text('czy to dziala')]]

window = sg.Window('chess', layout)

#figurki czarne
pionek_b = sg.Image('pionek_b.png')
wieza_b = sg.Image('wieza_b.png')
kon_b = sg.Image('kon_b.png')
goniec_b = sg.Image('goniec_b.png')
hetman_b = sg.Image('hetman_b.png')
krol_b = sg.Image('krol_b.png')



while True:
	event, values = window.read()

	if event in (sg.WIN_CLOSED, 'Exit'):
		break
