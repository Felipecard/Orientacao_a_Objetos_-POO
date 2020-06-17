
class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def muda_lado(self, novo_lado):
        self.lado = novo_lado

    def retorna_lado(self):
        print(f'O lado do quadrato tem {self.lado} cm')

    def area(self):
        print(f' O quadrado tem como área {self.lado * self.lado} cm')


# MAIN
# objeto:
quad1 = Quadrado(10)

# programa:
print('------------------')

resp = str(input('O quadrado tem 10 cm de lado, gostaria de mudar o lado? [s/n]'))
if resp == 's':
    novo_lado = int(input('Pra quantos Cm gostaria de modificar o lado? '))
else:
    novo_lado = 10

quad1.muda_lado(novo_lado)
print('------------------')
quad1.retorna_lado()
print('------------------')
quad1.area()
