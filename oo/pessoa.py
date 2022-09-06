class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'ola {id(self)}'

if __name__ == '__main__':
    danilo = Pessoa(nome='Danilo', idade=7)
    rafael = Pessoa(nome='Rafael', idade=4)
    claudio = Pessoa(danilo, rafael, nome='Claudio')
    marcelo = Pessoa(nome='Marcelo', idade=35)

    print(marcelo.cumprimentar())
    print(marcelo.nome, marcelo.idade)
    marcelo.sobrenome = 'Magario'
    print(marcelo.sobrenome)
    del marcelo.filhos
    print('-------------------------------------------')
    for filho in claudio.filhos:
        print(filho.nome, filho.idade)
    print('-------------------------------------------')
    marcelo.olhos = 1
    print(f'Número de olhos das pessoas: {Pessoa.olhos}')
    print(f'Número de olhos do Marcelo: {marcelo.olhos}')
    print(f'Número de olhos do Claudio: {claudio.olhos}')
    print(f'Número de olhos do Danilo: {danilo.olhos}')
    print('-------------------------------------------')
    print(claudio.__dict__)
    print(marcelo.__dict__)
    print('-------------------------------------------')



