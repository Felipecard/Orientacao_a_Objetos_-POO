
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimi_valores(self):
        return print(f'{self.x} e {self.y}')

    def centro(self):
        x_centro = (self.largura.x + self.altura.x) / 2.0
        y_centro = (self.largura.y + self.altura.y) / 2.
        print(x_centro, y_centro)

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura




# OBJ DA CLASSE PONTO:
x1 = 2
y1 = 3
ponto1 = Ponto(x1, y1)

# OBJ DA CLASSE RATANGULO:
retang1 = Retangulo(10, 5)

# MAIN
ponto1.imprimi_valores()
print(f'Ponto central é {Ponto.centro()}')

