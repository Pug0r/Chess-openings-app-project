import PySimpleGUI as sg
sg.theme('LightGreen')

# adding this comment to see if VCS works

menu_def = [['settings', ['graphics', ['option 1', 'option 2', ], 'add an opening'], ],]
           
layout = [[sg.Menu(menu_def)],
		[sg.VPush()],
		[sg.Push(), sg.Text('title'), sg.Push()],
		[sg.Push(), sg.Button('practice random opening', key='-random-'), sg.Push()],
		[sg.Push(), sg.Button('choose opening to practice', key='-choose-'), sg.Push()],
		#[sg.Push(), sg.Button('settings', key = '-settings-'), sg.Push()],
		[sg.VPush()]]



#layout_settings = [[sg.VPush()],
			#[sg.Push(), sg.Button('add an opening', key = '-add-'), sg.Push()],
			#[sg.Push(), sg.Button('change graphics', key = '-graphics-'), sg.Push()],
			#[sg.Push(), sg.Button('back to menu', key = '-back-'), sg.Push()],
			#[sg.VPush()]]

window = sg.Window('awesome chess!', layout, size = (500, 500))

#def settings():
	#window2 = sg.Window('super szachy!: settings', layout_settings, size = (500, 500))
	#event, values = window2.read()
	#if event=='-back-':
		#window2.close()
		#window.reappear()


while True:
	event, values = window.read()
	if event in (sg.WIN_CLOSED, 'Cancel'):
		break
	elif event == '-random-':
		pass
	elif event == '-choose-':
		pass
	#elif event == '-settings-':
		#pass
	
window.close()
