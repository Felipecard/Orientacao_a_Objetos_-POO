
# ASSOCIACAO - Usa outro OBJ | AGREGACAO - Tem outro OBJ | COMPOSICAO - É dono de outro OBJ | HERANCA - É outro OBJ


class Carrinho_de_compras:                           # Essa classe pode existir sozinha, mas ela precisa da class produto pra funcionar
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)      # AQUI ESTA A JUNCAO DAS CLASSES

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total


class Produto:                                     # Funciona tb sozinha e nao depende em nada da class carrinho
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


# OBJ DA CLASS CARRINHO DE COMPRAS:
carrinho = Carrinho_de_compras()

# OBJ da CLASS PRODUTO:
p1 = Produto('Camiseta', 50)
p2 = Produto('iPhone', 1250)
p3 = Produto('Caneca', 15)

# MAIN
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)

carrinho.lista_produto()
print(carrinho.soma_total())