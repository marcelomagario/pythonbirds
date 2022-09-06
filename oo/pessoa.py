class Pessoa:
    def cumprimentar(self):
        return f'ola {id(self)}'

if __name__ == '__main__':
    p, p2 = Pessoa(), Pessoa()
    print(id(p))
    print(p.cumprimentar())
    print()
    print(id(p2))
    print(p2.cumprimentar())
