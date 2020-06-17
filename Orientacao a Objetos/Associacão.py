
class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None
        
    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo...')


class Maquina_escrever:
    def escrever(self):
        print('Maquina está escrevendo...')


# OBJ:
escritor = Escritor('Joãozinho')
caneta = Caneta('BIC')
maquina = Maquina_escrever()

# MAIN
print(escritor.nome)
print(caneta.marca)
maquina.escrever()
print('----------')

# **ASSOCIACAO
escritor.ferramenta = caneta   # Enviando a classe Caneta inteira para o atributo: __ferramenta (qui dentro: self.__ferramenta = None)
escritor.ferramenta.escrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()