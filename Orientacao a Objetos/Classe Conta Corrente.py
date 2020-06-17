
class Conta_Corrente:
    def __init__(self, numero, nome, saldo=0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome = novo_nome
        print(f'O nome foi alterado para {self.nome}')

    def deposito(self, deposito):
        self.saldo = self.saldo + deposito
        print(f'{self.nome}, foi depositado R${deposito}, o saldo total agora é: R${self.saldo}')

    def saque(self, saque):
        self.saldo = self.saldo - saque
        print(f'{self.nome}, foi retirado R${saque}, o saldo total agora é: R${self.saldo}')


# Formando um Objeto
n_conta = int(input('Numero da conta: '))
correntista = str(input('Nome: '))
saldo_total = float(input('Saldo Total: '))

# Objeto
conta1 = Conta_Corrente(n_conta, correntista, saldo_total)
conta2 = Conta_Corrente(758, 'Lukita')

# MAIN
print('--------------------------')
print(conta2.nome, conta2.saldo)  # Para apresentar os dados basta fazer isso
print('--------------------------')

conta1.alterarNome('Cesar Gadelha')
conta2.alterarNome('Likita da Galera')
print('--------------------------')

conta1.deposito(20.0)
conta2.deposito(200.0)
print('--------------------------')

conta1.saque(50.0)
conta2.saque(100.0)
print('--------------------------')

print(conta2.nome, conta2.saldo)  # Para apresentar os dados basta fazer isso