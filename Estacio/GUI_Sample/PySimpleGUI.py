import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [ [sg.Text('Texto na linha 1')],
    [sg.Text('Entre com um texto na linha 2'), sg.InputText()],
    [sg.Button('Ok'), sg.Button('Cancel')] ]
window = sg.Window('Bem-Vindo ao PySimpleGUI', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print('Você entrou com: ', values[0])

window.close()