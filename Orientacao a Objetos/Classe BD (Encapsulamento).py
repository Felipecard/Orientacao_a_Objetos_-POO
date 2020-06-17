
class Base_de_dados:
    def __init__(self):
        self._dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id: nome}
        else:
            self._dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self._dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self._dados['clientes'][id]

# OBJ:
bd = Base_de_dados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')

# MAIN
# bd.dados = 'Uma outra coisa' | So pra mostrar q isso quebraria o programa inteiro..
                             # | Por isso eh bom colocar o bd.dados cpmo privado (Colocando um ou dois underline)
                             # | _ = Protectes | __ = private
bd.lista_clientes()
bd.inserir_cliente(4, 'Augusto')
print('-------')
bd.lista_clientes()

