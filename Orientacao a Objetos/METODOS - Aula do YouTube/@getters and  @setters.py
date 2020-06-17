# https://www.youtube.com/watch?v=PGXwNophTOQ&list=PLbIBj8vQhvm34qAAEEH_PdL2tMG9rz-P7&index=4

# Getter - Obtem valor
# Setter - Configura um valor

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome                # Sempre q o contrutor ocorrer eles vao passar pelo getter e setter antes dessa linha, funciona como filtro
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter
    @property
    def preco(self):
        return self._preco          # Por convencao: Colocar um _ antes, para nao fazer um loop estranho, mas funcuinaria

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):                     # Agora o R$ vai funcionar
            valor = float(valor.replace('R$', ''))     # Entao o getter e setter acabam sendo uma protecao pro atributo

        self._preco = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()



p1 = Produto('CAMISETA', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

# p2 = Produto('Caneca', 'R$ 15' # Assim daria erro, por isso vamos utilizar o gatter e setter)
# p2.desconto(10)
# print(p2.preco)

p2 = Produto('CANECA', 'R$15')     # Conseguir mudar o nome com Getter e o setter,
p2.desconto(10)
print(p2.nome, p2.preco)