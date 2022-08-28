import PySimpleGUI as sg

APP_NAME = "Chess Openings Coach"
sg.theme('LightGreen')

menu_def = ['settings', ['add an opening', ['graphics', ['option 1', 'option 2', 'option 3']]]]

menu_def = [['settings', ['graphics', ['option 1', 'option 2', ], 'add an opening'], ], ]
# dalabys rade zrobic tak zeby settings bylo w ten sam sposob wyswietlone jak reszta? w sensie zeby nie bylo tak u gory
layout = [[sg.Menu(menu_def)],
          [sg.VPush()],
          [sg.Push(), sg.Text('tu powinna byc grafika z tytulem'), sg.Push()],
          [sg.Push(), sg.Button('practice random opening', key='-random-'), sg.Push()],
          [sg.Push(), sg.Button('choose opening to practice', key='-choose-'), sg.Push()],
          # [sg.Push(), sg.Button('settings', key = '-settings-'), sg.Push()],
          [sg.VPush()]]

# layout_settings = [[sg.VPush()],
# [sg.Push(), sg.Button('add an opening', key = '-add-'), sg.Push()],
# [sg.Push(), sg.Button('change graphics', key = '-graphics-'), sg.Push()],
# [sg.Push(), sg.Button('back to menu', key = '-back-'), sg.Push()],
# [sg.VPush()]]

window = sg.Window(APP_NAME, layout, size=(500, 500))

# def settings():
# window2 = sg.Window('super szachy!: settings', layout_settings, size = (500, 500))
# event, values = window2.read()
# if event=='-back-':
# window2.close()
# window.reappear()


while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    elif event == '-random-':
        pass
    elif event == '-choose-':
        pass
# elif event == '-settings-':
# pass

window.close()
