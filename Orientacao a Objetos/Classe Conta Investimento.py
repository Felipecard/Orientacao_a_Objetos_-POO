
class Conta_investimento:
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo_inicial = saldo_inicial
        self.taxa_juros = taxa_juros

    def adiciona_juros(self):
        valor_juros = (self.saldo_inicial * self.taxa_juros) / 100
        self.saldo_inicial = self.saldo_inicial + valor_juros
        print(f'O salto atual é R$ {self.saldo_inicial}')


# OBJ:
poupanca1 = Conta_investimento(1000, 3)

# MAIN:
poupanca1.adiciona_juros()
poupanca1.adiciona_juros()
poupanca1.adiciona_juros()
poupanca1.adiciona_juros()
poupanca1.adiciona_juros()
