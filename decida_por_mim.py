#Faça uma pergunta para o programa e ele terá q te dar uma resposta

import random

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            "Com certeza, você deve fazer isso!",
            "não sei, você que sabe",
            "Não faz isso Não!",
            "acho que tá na hora certa!"
        ]

    def Iniciar(self):
        input("Faça sua pergunta: ")
        print(random.choice(self.respostas))

decida = DecidaPorMim()
decida.Iniciar()