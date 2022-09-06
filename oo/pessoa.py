class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'ola {id(self)}'

if __name__ == '__main__':
    danilo = Pessoa(nome='Danilo', idade=7)
    rafael = Pessoa(nome='Rafael', idade=4)
    claudio = Pessoa(danilo,rafael, nome='Claudio')
    for filho in claudio.filhos:
        print(filho.nome, filho.idade)


    p = Pessoa('Marcelo', 35)
    print(p.cumprimentar())
    print(p.nome, p.idade)
    p.nome = 'Irena'
    print(p.nome, p.idade)

