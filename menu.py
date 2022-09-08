import PySimpleGUI as sg
import os
import random
from threading import Thread
from openings import *
import board

APP_NAME = "Chess Openings Coach"
ABOUT_TEXT = "This app is designed to help You practise & memorise various chess openings. \nIt uses PySimpleGUI, " \
             "tkinter and Pychess. \nDeveloped by Aleksander Pugowski and Marta Niemiec "

GRAPHICS_NO = 1
sg.theme('LightGreen')

layout_start = [[sg.VPush()],
                [sg.Push(), sg.Image('tytul2.png'), sg.Push()],
                [sg.Text('\n')],
                [sg.Push(), sg.Button('practice random opening', key='-random-', font='NSimSun'), sg.Push()],
                [sg.Push(), sg.Button('choose opening to practice', key='-choose-', font='NSimSun'), sg.Push()],
                [sg.Push(), sg.Button('settings', key='-settings-', font='NSimSun'), sg.Push()],
                [sg.Push(), sg.Button('about', key='-about-', font='NSimSun'), sg.Push()],
                [sg.VPush()]]

layout_settings = [[sg.VPush()],
                   [sg.Text('\n \n')],
                   [sg.Push(), sg.Button('add an opening', key='-add-', font='NSimSun'), sg.Push()],
                   [sg.Push(), sg.Button('change graphics', key='-graphics-', font='NSimSun'), sg.Push()],
                   [sg.Push(), sg.Button('back to menu', key='-back-', font='NSimSun'), sg.Push()],
                   [sg.VPush()]]

option1 = sg.Image('graphics/figures1.png', visible=False, key='option1')
option2 = sg.Image('graphics/figures2.png', visible=False, key='option2')

layout_graphics = [[sg.VPush()],
                   [sg.Text('\n \n')],
                   [sg.Push(), sg.Button('option 1', key = '-graphics1-', font='NSimSun'), sg.Push()],
                   [sg.Push(), sg.Button('option 2', key = '-graphics2-', font='NSimSun'), sg.Push()],
                   [sg.Push(), sg.Text('A preview of your choice will be displayed here', key='-preview-'), option1, option2, sg.Push()], #tu chce zeby wyswietlaly sie pionki z opcji
                   [sg.Push(), sg.Text('chosen: option 1', key='-choice-'), sg.Push()],
                   [sg.Push(), sg.Button('back', key='-graphics_back-', font='NSimSun'), sg.Push()]]


layout_choose = [[sg.Button(button_text=OPENING_NUMBERS[i]['name'], font='NSimSun', key=i+1)] for i in range(len(OPENING_NUMBERS))]

layout_choose2 = [[sg.VPush()],
                  [sg.Push(), sg.Button('back to main manu', font='NSimSun', key='-back_choose-')]]

layout = [[sg.pin(sg.Column(layout_start, key='-start-', visible=True)), sg.pin(sg.Column(layout_settings, key='-settings_window-', visible=False)), sg.pin(sg.Column(layout_graphics, key='-graphics_window-', visible=False)), sg.pin(sg.Column(layout_choose, key='-choose_window-', visible=False, scrollable=True, vertical_scroll_only=True)), sg.pin(sg.Column(layout_choose2, key='-choose_window2-', visible=False))]]

window = sg.Window(APP_NAME, layout, element_justification='c', size=(500, 350))


def preview(n):
    window['-preview-'].update(visible=False)
    window['option1'].update(visible=False)
    window['option2'].update(visible=False)
    window[f'option{n}'].update(visible=True)


def choose_graphics(n):
    window['-choice-'].update(f'chosen: option {n}')


while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        pass
    elif event == '-random-':
        arg = random.choice(list(OPENING_NUMBERS.keys()))
        t = Thread(target=lambda: os.system("python board.py {args} {graphics}".format(args=arg, graphics=GRAPHICS_NO)))
        t.start()
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
        GRAPHICS_NO = 1
    if event == '-graphics2-':
        preview(2)
        choose_graphics(2)
        GRAPHICS_NO = 2
    elif event == '-add-':
        sg.popup_no_buttons("For the time being, to add an opening go to program files/openings and "
                            "simply type in the opening, following the format", title='How to add an opening?', modal=False)
    elif event == '-about-':
        sg.popup_no_buttons(ABOUT_TEXT, title=APP_NAME, modal=False)

    if event in [i+1 for i in range(len(OPENING_NUMBERS))]:
        print(event)
        a = Thread(target=lambda: os.system("python board.py {args} {graphics}".format(args=int(event)-1, graphics=GRAPHICS_NO)))
        a.start()

window.close()
