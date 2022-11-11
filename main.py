import PySimpleGUI as sg

from funcoes import calcular_consumo


sg.theme('Light Green 5')

layout = [

    [sg.Text('Quantos litros de água você precisa beber por dia?')],
    [sg.Text('Insira o seu peso ao lado:'), sg.InputText(key="peso"), sg.Text('Kg')],
    [sg.Button('Calcular')],
    [sg.Text('', key='consumo')]

]

window = sg.Window('Calculadora', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Calcular':
        peso = values['peso']
        consumo = calcular_consumo(peso)
        window['consumo'].update('Você precisa beber {:.2f} litros de água por dia!'.format(consumo))


window.close()

