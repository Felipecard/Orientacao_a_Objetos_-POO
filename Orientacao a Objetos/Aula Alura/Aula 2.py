
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print('Chamando @propety nome()')
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print('Chamando setter(muda algo) nome()')    #Criou um set sem colocar ele na frente: def set_nome():
        self.__nome = nome


#objeto:
cliente = Cliente('nico')


print(cliente.nome)

cliente.nome = 'marco'
print(cliente.nome)