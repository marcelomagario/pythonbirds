""""
Você deve criar uma classe Carro que vai ter dois atributos compostos por outras duas classes:
1-) Motor
2-) Direção

O Motor é responsável por controlar a velocidade.
Ele oferece os seguintes atributos:
1)- Atributo de dados velocidade
2) Método acelerar, que deverá incrementar a velocidade de uma unidade.
3) Método frear que deverá decrementar a velocidade em duas unidades.

A Direção é responsável por controlar a direção.
Ela oferece os seguintes atributos:
1-) Valor de direção com valores possíveis: Norte, Sul, Leste e Oeste.
2-) Método girar_a_direita
3-) Método girar_a_esquerda

  N
O   L
  S

    Exemplo:
    # Testando Motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    0

    # Testando Direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'

"""


class Motor:

    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade = 0 if self.velocidade <= 1 else self.velocidade - 2

    def calcular_velocidade(self):
        print(self.velocidade)


class Direcao:

    direcoes = {0: 'Norte', 1: 'Leste', 2: 'Sul', 3: 'Oeste'}

    def __init__(self, posicao=0):
        self.posicao = posicao
        self.valor = self.direcoes[posicao]

    def girar_a_direita(self):
        self.posicao = 0 if self.posicao == 3 else self.posicao + 1
        self.valor = self.direcoes[self.posicao]

    def girar_a_esquerda(self):
        self.posicao = 3 if self.posicao == 0 else self.posicao - 1
        self.valor = self.direcoes[self.posicao]

    def calcular_direcao(self):
        return self.valor


class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_velocidade(self):
        self.motor.calcular_velocidade()

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

    def calcular_direcao(self):
        return self.direcao.calcular_direcao()
#
#
#
if __name__ == '__main__':

    # instanciando o objeto
    pedal = Motor()
    volante = Direcao()
    mitsi = Carro(motor=pedal, direcao=volante)
#     # Testando o volante
#     mitsi.direcao.girar_a_esquerda()
#     mitsi.direcao.girar_a_esquerda()
#     print(mitsi.direcao.mostrar_a_direcao())
#     # Testando o motor
#     mitsi.motor.frear()
#     mitsi.motor.acelerar()
#     mitsi.motor.acelerar()
#     mitsi.motor.acelerar()
#     mitsi.motor.acelerar()
#     mitsi.motor.acelerar()
#     mitsi.motor.frear()
#     print(mitsi.motor.mostrar_velocidade())
#
#
