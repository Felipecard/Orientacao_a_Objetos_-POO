#def cria_conta(numero, titular, saldo, limite):
#    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
#    return conta

#def deposita(conta, valor):
#    conta["saldo"] += valor

#def saca(conta, valor):
#    conta["saldo"] -= valor

#def extrato(conta):
#    print("Saldo {}".format(conta["saldo"]))


# ---------------------------------------- DIFERENCA DE PROCEDURAL PARA OO (a baixo)

class Conta:
    def __init__(self, numero, titular, saldo, limite): # __init__ = Funcao construtora
        print(f'Contruindo Objeto... {self}') # self = referencia - onde esta guardado na memoria
        self.__numero = numero     # numero = Atributo
        self.__titular = titular  # Atributo - Quando coloca (__) na frente do atributo, ele é privado e nao pode ser acessado e qualquer maneira.. como: conta.saldo = 60 (assim eh muito feio e errado) mas funcionaria
        self.__saldo = saldo     # Atributo
        self.limite = limite    # Atributo *Apenas esse nao coloquei privado (sem motivo)


    def extrato(self):               # Isso é um metodo da Classe conta
        print(f'Saldo {self.__saldo} do titular {self.__titular}')

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):      # Tem esse __ pq nao quero esse metodo sendo usado fora da classe.. apenas dentro dela
        valor_disponivel_a_sacar = self.__saldo + self.__limite    # Esse codigo podeficar no: def saca() .. mas aqui fica mais limpo
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print(f'O valor {valor} passou do limite')

    def transfere(self, valor, destino):     # def transfere(self, valor, origem, destino):
        self.saca(valor)                     #     origem.saca(valor)
        destino.deposita(valor)              #     destino.deposita(valor)           (assim tb funcionaria, mas o jeito mais adequado é como ficou)

    def get_saldo(self):             # O get retorna algo!
        return self.__saldo

    def get_titular(self):
        return self.__titular             # reforçando que tanto para acessar quanto para alterar características de um objeto precisamos criar métodos.

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):     # Um set nunca reotna nada, ele muda algo!
        self.__limite = limite

    @staticmethod                      # metodo estatico, sem o self.. pq ele fica pertencendo a classe..  nao ao objeto.. por isso nao tem o self
    def codigo_banco():
        return '001'

    @staticmethod
    def codigo_banco():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

conta = Conta(123, 'Nico', 55.5, 1000.0) # Criando um objeto chamado conta
conta2 = Conta(565, 'Marco', 100.0, 1000.0) # Criando um objeto chamado conta2



print('Mostrando dados especificos:')
print(conta._Conta__saldo) # Teria q mudar aqui para essa formatacao tb.. colocando: _Conta__ (Ou seja, nao acessa diretamente pq ele virou privado)
print(conta2._Conta__titular)
print('-=' * 30)

conta.extrato()
conta2.extrato()

print('-=' * 30)
print('Depositando e sacando')
conta.deposita(44.5)
conta2.saca(50)

conta.extrato()
conta2.extrato()

print('-=' * 30)
print('Transferindo dinheiro da conta 1 para a 2:')
conta2.transfere(10.0, conta)  # A variavel SELF nao precisa passar pq ja é implicito quando se coloca 'conta2.'
conta2.extrato()
conta.extrato()

print('-=' * 30)
v = conta.get_saldo()
print(v)
print('Novo limite alterado:')
# conta.set_limite(5000.0)    - Como estava antes sem o @propety e @limite.setter
# print(conta.get_limite())
print(conta.limite)
conta.limite = 2000.0
print(conta.limite)

print('-=' * 30)
conta.saca(2500)
conta.extrato()

print('-=' * 30)
print('Chamando o metodo direto da classe (estatico)')           # mas aqui vc nao esta fugindo da orientacao a objetos (devem ser usados com cautela)
print(Conta.codigo_banco())
print('Chamando o metodo direto da classe (estatico) com dicionario')
codigos = Conta.codigo_banco()
print(codigos['Caixa'])