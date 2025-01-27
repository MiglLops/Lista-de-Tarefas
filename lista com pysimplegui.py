import PySimpleGUI as sg

def criar_janela():
    sg.theme("DarkBlue4")
    interface = [
    [sg.Checkbox(""), sg.Input(size=(50, 1))]
    ]

    layout = [
        [sg.Frame('Tarefas', layout=interface, key='container')],
        [sg.Button('Nova Tarefa'), sg.Button('Resetar'), sg.Button('Desmarcar Tudo')]
    ]
    return sg.Window('Lista de Tarefas',layout,finalize=True)

janela = criar_janela()
while True:
    event, value = janela.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Nova Tarefa':
        janela.extend_layout(janela['container'], [[sg.Checkbox(''),sg.Input('')]])
    elif event == 'Resetar':
        janela.close()
        janela = criar_janela()