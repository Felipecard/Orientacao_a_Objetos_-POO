
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando...')


class Professor(Pessoa):
    def lecionar(self):
        print(f'{self.nomeclasse} dando aula...')

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} estudando...')


# MAIN:
p1 = Professor('Luiz', 45)
p1.falar()
p1.lecionar()

print('-----')
a1 = Aluno('Marquinho', 12)
a1.falar()
a1.estudar()

print('-----')
p1 = Pessoa('Maicon', 43)
p1.falar()