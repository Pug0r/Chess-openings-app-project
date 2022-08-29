import PySimpleGUI as sg

APP_NAME = "Chess Openings Coach"
sg.theme('LightGreen')


#menu_def = [['settings', ['graphics', ['option 1', 'option 2', ], 'add an opening'], ], ]

layout = [[sg.VPush()],
          [sg.Push(), sg.Text('tu powinna byc grafika z tytulem'), sg.Push()],
          [sg.Push(), sg.Button('practice random opening', key='-random-'), sg.Push()],
          [sg.Push(), sg.Button('choose opening to practice', key='-choose-'), sg.Push()],
          [sg.Push(), sg.Button('settings', key = '-settings-'), sg.Push()],
          [sg.Push(), sg.Button('about', key = '-about-'), sg.Push()],
          [sg.VPush()]]



window = sg.Window(APP_NAME, layout, size=(500, 500))


def settings():
    layout_settings = [[sg.VPush()],
                       [sg.Push(), sg.Button('add an opening', key='-add-'), sg.Push()],
                       [sg.Push(), sg.Button('change graphics', key='-graphics-'), sg.Push()],
                       [sg.Push(), sg.Button('back to menu', key='-back-'), sg.Push()],
                       [sg.VPush()]]
    window2 = sg.Window(APP_NAME, layout_settings, size = (500, 500))
    event, values = window2.read()
    if event == '-back-':
        window2.disappear()
        window.reappear()


while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    elif event == '-random-':
        pass
    elif event == '-choose-':
        pass
    elif event == '-settings-':
        window.disappear()
        settings()
    elif event == '-about-': #mozna tu opisac pokrotce o co chodzi (ale zrobilam to glownie zeby zobaczyc jak dziala popup xd)
        sg.popup_no_buttons('this app blablablablabla', title = APP_NAME, modal = False)

window.close()
