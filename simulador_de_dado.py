# Simulador de dado
# Simular o uso de um dado, gerando um valor de 1 até 6
import random
import PySimpleGUI as sg


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = "Você gostaria de gerar um novo valor para o dado?"
        #Criar uma tela de visualização para o jogo com PySimpleGUI
        # Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'),sg.Button('não')]
        ]

    def Iniciar(self):
         # criar uma janela
        janela = sg.Window('Simulador de Dado',layout=self.layout)
        # ler os valores da tela
        self.eventos, self.valores = janela.Read()
        # fazer alguma coisa com esses valores
        
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValorDodado()
            elif self.eventos == 'não' or self.eventos == "n":
                print('Agradecemos sua participação!')
            else:
                print('Favor digitar sim ou não...')
        except:
                print("Ocorreu um erro ao receber sua resposta...")

    def GerarValorDodado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDeDado()
simulador.Iniciar()
