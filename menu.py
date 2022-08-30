import PySimpleGUI as sg
#juz dziala w jednym okienku ale zepsulo sie wysrodowanie>:(( naprawiam je
# czadowy pomysl z tym about<3
APP_NAME = "Chess Openings Coach"
sg.theme('LightGreen')


layout_start = [[sg.VPush()],
                [sg.Push(), sg.Text('tu powinna byc grafika z tytulem'), sg.Push()],
                [sg.Push(), sg.Button('practice random opening', key='-random-', font = 'Helvetica'), sg.Push()],
                [sg.Push(), sg.Button('choose opening to practice', key='-choose-', font = 'Helvetica'), sg.Push()],
                [sg.Push(), sg.Button('settings', key = '-settings-', font = 'Helvetica'), sg.Push()],
                [sg.Push(), sg.Button('about', key = '-about-', font = 'Helvetica'), sg.Push()],
                [sg.VPush()]]

layout_settings = [[sg.VPush()],
                   [sg.Push(), sg.Button('add an opening', key='-add-', font = 'Helvetica'), sg.Push()],
                   [sg.Push(), sg.Button('change graphics', key='-graphics-', font = 'Helvetica'), sg.Push()],
                   [sg.Push(), sg.Button('back to menu', key='-back-', font = 'Helvetica'), sg.Push()],
                   [sg.VPush()]]

layout_graphics = [[sg.VPush()],
                   [sg.Push(), sg.Button('option 1', key = '-graphics1-', font = 'Helvetica'), sg.Push()],
                   [sg.Push(), sg.Button('option 2', key = '-graphics2-', font = 'Helvetica'), sg.Push()],
                   [sg.Push(), sg.Text('preview:'), sg.Push()], #tu chce zeby wyswietlaly sie pionki z opcji
                   [sg.Push(), sg.Button('back', key = '-graphics_back-', font = 'Helvetica'), sg.Push()]]

layout = [[sg.pin(sg.Column(layout_start, key = '-start-', visible = True)), sg.pin(sg.Column(layout_settings, key = '-settings_window-', visible = False)), sg.pin(sg.Column(layout_graphics, key = '-graphics_window-', visible = False))]]

window = sg.Window(APP_NAME, layout, element_justification='c', size=(500, 500))


def graphics():
    window['-settings_window-'].update(visible=False)
    window['-graphics_window-'].update(visible=True)


while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    elif event == '-random-':
        pass
    elif event == '-choose-':
        pass
    elif event == '-settings-':
        window['-settings_window-'].update(visible=True)
        window['-start-'].update(visible=False)
    if event == '-back-':
        window['-start-'].update(visible=True)
        window['-settings_window-'].update(visible=False)
    elif event == '-graphics-':
        graphics()
    if event == '-graphics_back-':
        window['-graphics_window-'].update(visible=False)
        window['-settings_window-'].update(visible=True)
    elif event == 'add':
        pass
    elif event == '-about-':
        sg.popup_no_buttons('This app was designed to blebleble', title = APP_NAME, modal = False)

window.close()
