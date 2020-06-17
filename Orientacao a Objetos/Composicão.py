
# Composicao eh a a ligacao mais forte entre classes, uma depende da outra.

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))    # Usamos a classe Endereco, pra *COMPOR a classe Cliente

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):            # So pra ver quando ele sumir da memoria.. pra aula msm
        print(f'{self.nome} FOI APAGADO')


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade}/ {self.estado }FOI APAGADO')


# OBJ:
cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')

cliente2 = Cliente('Maria', 52)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')

cliente3 = Cliente('João', 19)
cliente3.insere_endereco('Campinas', 'SP')

# MAIN
print(cliente1.nome)
cliente1.lista_enderecos()
print('-----------------')

print(cliente2.nome)
cliente2.lista_enderecos()
print('-----------------')

print(cliente3.nome)
cliente3.lista_enderecos()

print('#############################################')
# pra ver o coletor de de lixo do python.. apagando automatico(pra retirar de mmeoria do pc msm),
# como um depende do outro tudo eh apagado