#Chute o número
#Criar um algorítimo que gera um valor aleat´roio e eu tenho que ficar tentando o número até eu acertar

import random
import PySimpleGUI as sg

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        #layout
        self.layout = [
            [sg.Text('Seu Chute', size=(39,0))],
            [sg.Input(size=(18,0),key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(39,10))]
            ]
        #criar uma janela
        self.janela = sg.Window('Chute o numero de 1 a 100!', layout=self.layout)
        self.GerarNumeroAleatorio()
        
        try:
            while True:
                #receber valores
                self.evento, self.valores = self.janela.Read()
                #fazer alguma coisa com estes valores
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um valor mais baixo!')
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Chute um valor mais alto!')
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print('Parabéns, você acertou!')
                            break
                if self.evento == sg.WIN_CLOSED:
                    break                 
        except:
            print('Favor digitar apenas números inteiros!')
            self.Iniciar()

    
    def GerarNumeroAleatorio(self):
       self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)


chute = ChuteONumero()
chute.Iniciar()