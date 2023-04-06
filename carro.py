class Carro:

    def __init__(self,marca,modelo,cor,combustivel):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel
        self.velocidade = 0

        self.ligado = False

    def ligar(self):
        if self.ligado:
            print("carro ja esta ligado. nada a fazer")
        else:
             print("Carro ligado")
             self.ligado = True

        

    def desligar(self):
         if self.ligado:
            self.ligado = False
            print("Carro desligado")
         else:
              print("carro ja esta ligado. nada a fazer")


    def acelerar(self):
        if self.ligado:
            self.velocidade += 1
            print(f"A velocidade {self.velocidade}")
        else:
            print("Nao pode acelerar, carro desligado")


    def freae(self):
        if self.ligado:
            self.velocidade -= 1
            print(f"A velocidade {self.velocidade}")
        else:
            print("Nao pode frear, carro desligado")
    