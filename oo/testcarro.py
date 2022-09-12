# Example of Unit Test
from unittest import TestCase
from oo.carro import Motor, Direcao


class CarroTestCase(TestCase):
    def test_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def test_direcao_inicial(self):
        direcao = Direcao()
        self.assertEqual('Norte', direcao.valor)



