class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    luciano = Pessoa(nome='Luciano')
    julio = Pessoa(nome='julio')
    marcelo = Pessoa(julio, nome='marcelo')
    print(Pessoa.cumprimentar(marcelo))
    print(id(marcelo))
    print(marcelo.cumprimentar())
    print(marcelo.nome)
    print(marcelo.idade)
    print(marcelo.filhos)
    for filho in marcelo.filhos:
        print(filho.nome)


