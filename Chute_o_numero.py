#Chute o número
#Criar um algorítimo que gera um valor aleat´roio e eu tenho que ficar tentando o número até eu acertar

import random

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100

    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        if int(self.valor_do_chute) > self.valor_aleatorio:
            print('Chute um valor mais baixo!')
            self.PedirValorAleatorio()
        elif int(self.valor_do_chute) < self.valor_aleatorio:
            print('Chute um valor mais alto!')
            self.PedirValorAleatorio()

    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um número: ')

    def GerarNumeroAleatorio(self):
       self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)
