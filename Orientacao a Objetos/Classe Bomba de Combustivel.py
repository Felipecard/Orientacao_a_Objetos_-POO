
# Gasolina = R$ 4.70
# Alcool = R$ 3.40

class Bomba:
    def __init__(self, tipo, valor='x', quantidade='x'):
        self.tipo = tipo
        self.valor = valor
        self.quantidade = quantidade
        self.gasolina = 4.70
        self.alcool = 3.40

    def abastecer_por_valor(self):
        if self.tipo == 'g':
            self.quantidade = self.valor / self.gasolina
            total = self.gasolina * self.quantidade
            print('GASOLINA | por valor:')
            print(f'R$ ({self.gasolina})G x {self.quantidade} Litros = TOTAL A PAGAR: R$ {total}')
        if self.tipo == 'a':
            self.quantidade = self.valor / self.alcool
            total = self.alcool * self.quantidade
            print('ALCOOL | por valor:')
            print(f'R$ ({self.alcool})A x {self.quantidade} Litros = TOTAL A PAGAR: R$ {total}')

    def abastecer_por_quantidade(self):
        if self.tipo == 'g':
            self.valor = self.quantidade * self.gasolina
            print('GASOLINA | por quantidade:')
            print(f'R$ ({self.gasolina})G x {self.quantidade} Litros = TOTAL A PAGAR: R$ {self.valor}')
        if self.tipo == 'a':
            self.valor = self.quantidade * self.alcool
            print('ALCOOL | por quantidade:')
            print(f'R$ ({self.alcool})A x {self.quantidade} Litros = TOTAL A PAGAR: R$ {self.valor}')


    def alterar_valor(self, valor):
        self.valor = valor

    def altera_tipo(self, tipo):
        if tipo == 'g':
            self.tipo = 'g'
        if tipo == 'a':
            self.tipo = 'a'


    def altera_quantidade(self, quantidade):
        self.quantidade = quantidade




# OBJ:
cliente1 = Bomba('a', 100, 21.27)

# MAIN:
cliente1.altera_tipo('g')
cliente1.abastecer_por_valor()
print('------------')
cliente1.altera_tipo('a')
cliente1.abastecer_por_quantidade()
print('------------')
cliente1.altera_tipo('g')
cliente1.alterar_valor(150.0)
cliente1.abastecer_por_valor()
print('------------')
cliente1.altera_tipo('a')
cliente1.altera_quantidade(50)
cliente1.abastecer_por_quantidade()
print('------------')