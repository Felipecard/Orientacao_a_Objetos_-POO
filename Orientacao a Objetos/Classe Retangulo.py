
class Retangulo:
    def __init__(self, comp, larg):
        self.comp = comp
        self.larg = larg

    def muda_lados(self, muda_comp, muda_larg):
        self.comp = muda_comp
        self.larg = muda_larg

    def valor_lados(self):
        print(f'Os lados do Retangulo são: {self.comp} cm de comp e {self.larg} cm de largura')

    def area(self):
        print(f'A area do retangulo é: {self.comp} x {self.larg} = {self.comp * self.larg}')

    def perimetro(self):
        p = (self.comp + self.larg) * 2
        return f'A Perimetro do retangulo é: {self.comp} + {self.larg} + {self.comp} + {self.larg} = {p}'


# MAIN
# objeto:
retangulo1 = Retangulo(10, 5)

# rodando:
print('------------------------------------------------------------------------------')
muda_comp = int(input('O retanfulo tem 10 cm de comprimento, deseja mudar pra quanto?'))
muda_larg = int(input('O retanfulo tem 5 cm de largura, deseja mudar pra quanto?'))
retangulo1.muda_lados(muda_comp, muda_larg)

print('------------------------------------------------------------------------------')
retangulo1.valor_lados()
print('------------------------------------------------------------------------------')
retangulo1.area()
print('------------------------------------------------------------------------------')
print(retangulo1.perimetro())