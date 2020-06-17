from random import randint

class Pessoa:
    ano_atual = 2020

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def pega_ano_nascimento(self):                   # METODO DE INSTANCIA: Por isso ele precisa receber o self, o self
        print(self.ano_atual - self.idade)                    # se refere a propria instancia (objeto).


    @classmethod                                            # METODO DE CLASSE: Precisa estar decorado com o @classmethod.
    def por_ano_nascimento(cls, nome, ano_nascimento):      # Ele nao eh referente a instancia, mas sim a Classe
        idade = cls.ano_atual - ano_nascimento              #***Usa para coisas globais da classe****
        return cls(nome, idade)

    @staticmethod                                    # METODO ESTATICO: Eh como uma funcao normal, dentro do corpo dele nao pode usar Self e nem CLS
    def gera_id():                                   # Utiliza a intancia ou a classe pra utilizar ele.. como vemos no MAIN
        rand = randint(111, 999)
        return rand



# MAIN
p1 = Pessoa('Luiz', 32)
print(p1)
print(p1.nome, p1.idade)

p1.pega_ano_nascimento()
print(Pessoa.gera_id())
print(p1.gera_id())