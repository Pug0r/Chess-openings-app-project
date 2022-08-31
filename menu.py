import PySimpleGUI as sg

# czadowy pomysl z tym about<3
APP_NAME = "Chess Openings Coach"
sg.theme('LightGreen')


layout_start = [[sg.VPush()],
                [sg.Push(), sg.Text('\n \n tu powinna byc grafika z tytulem'), sg.Push()],
                [sg.Push(), sg.Button('practice random opening', key='-random-', font='Helvetica'), sg.Push()],
                [sg.Push(), sg.Button('choose opening to practice', key='-choose-', font='Helvetica'), sg.Push()],
                [sg.Push(), sg.Button('settings', key='-settings-', font='Helvetica'), sg.Push()],
                [sg.Push(), sg.Button('about', key='-about-', font='Helvetica'), sg.Push()],
                [sg.VPush()]]

layout_settings = [[sg.VPush()],
                   [sg.Text('\n \n')],
                   [sg.Push(), sg.Button('add an opening', key='-add-', font='Helvetica'), sg.Push()],
                   [sg.Push(), sg.Button('change graphics', key='-graphics-', font='Helvetica'), sg.Push()],
                   [sg.Push(), sg.Button('back to menu', key='-back-', font='Helvetica'), sg.Push()],
                   [sg.VPush()]]

# wrzucone tu obrazki sa tymczasowe, tylko dla sprawdzenia dzialania
# (option1 to bedzie obrazek z wszystkimi figurkami a option2 z innymi wgl)
option1 = sg.Image('graphics/figures1.png', visible=False, key='option1')
option2 = sg.Image('graphics/knight_b.png', visible=False, key='option2')

layout_graphics = [[sg.VPush()],
                   [sg.Text('\n \n')],
                   [sg.Push(), sg.Button('option 1', key = '-graphics1-', font='Helvetica'), sg.Push()],
                   [sg.Push(), sg.Button('option 2', key = '-graphics2-', font='Helvetica'), sg.Push()],
                   [sg.Push(), sg.Text('here will be displayed a preview of your choice', key='-preview-'), option1, option2, sg.Push()], #tu chce zeby wyswietlaly sie pionki z opcji
                   [sg.Push(), sg.Button('back', key='-graphics_back-', font='Helvetica'), sg.Push()]]

openings = ('name1', 'name2', 'name3', 'name4')

layout_choose = [[sg.Button(button_text=openings[i], font='Helvetica', key=f'opening{i}')] for i in range(len(openings))]

layout_choose2 = [[sg.VPush()],
                  [sg.Push(), sg.Button('back to main manu', font='Helvetica', key='-back_choose-')]]

layout = [[sg.pin(sg.Column(layout_start, key='-start-', visible=True)), sg.pin(sg.Column(layout_settings, key='-settings_window-', visible=False)), sg.pin(sg.Column(layout_graphics, key='-graphics_window-', visible=False)), sg.pin(sg.Column(layout_choose, key='-choose_window-', visible=False)), sg.pin(sg.Column(layout_choose2, key='-choose_window2-', visible=False))]]

window = sg.Window(APP_NAME, layout, element_justification='c', size=(500, 300))


def preview(n):
    window['-preview-'].update(visible=False)
    window['option1'].update(visible=False)
    window['option2'].update(visible=False)
    window[f'option{n}'].update(visible=True)


def choose_graphics(n):  # potem przy generowaniu tablicy przydaloby sie to jakos polaczyc
    pass


while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    elif event == '-random-':
        pass
    elif event == '-choose-':
        window['-choose_window-'].update(visible=True)
        window['-choose_window2-'].update(visible=True)
        window['-start-'].update(visible=False)
    if event == '-back_choose-':
        window['-choose_window-'].update(visible=False)
        window['-choose_window2-'].update(visible=False)
        window['-start-'].update(visible=True)
    elif event == '-settings-':
        window['-settings_window-'].update(visible=True)
        window['-start-'].update(visible=False)
    if event == '-back-':
        window['-start-'].update(visible=True)
        window['-settings_window-'].update(visible=False)
    elif event == '-graphics-':
        window['-settings_window-'].update(visible=False)
        window['-graphics_window-'].update(visible=True)
    if event == '-graphics_back-':
        window['-graphics_window-'].update(visible=False)
        window['-settings_window-'].update(visible=True)
    if event == '-graphics1-':
        preview(1)
        choose_graphics(1)
    if event == '-graphics2-':
        preview(2)
        choose_graphics(2)
    elif event == 'add':
        pass
    elif event == '-about-':
        sg.popup_no_buttons('This app was designed to blebleble', title=f'{APP_NAME}: about', modal=False)

window.close()
