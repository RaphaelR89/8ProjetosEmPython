#Faça uma pergunta para o programa e ele terá q te dar uma resposta

import random
import PySimpleGUI as sg

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            "Com certeza, você deve fazer isso!",
            "não sei, você que sabe",
            "Não faz isso Não!",
            "acho que tá na hora certa!"
        ]

    def Iniciar(self):
        #layout
        layout = [[sg.Text('Faça sua pergunta: ')],[sg.Input()],[sg.Output(size=(20,10))],[sg.Button('Decida por mim')]]
        #criar janela
        self.janela = sg.Window('Decida por mim!', layout=layout)
        while True:
            #ler os valores
            self.eventos, self.valores = self.janela.Read()
            #fazer algo com os valores
            if self.eventos == 'Decida por mim':
                print(random.choice(self.respostas))
                

decida = DecidaPorMim()
decida.Iniciar()