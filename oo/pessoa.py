class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'ola {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Marcelo', 35)
    print(p.cumprimentar())
    print(p.nome, p.idade)
    p.nome = 'Irena'
    print(p.nome, p.idade)

