
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def nome_func(self):
        print(self.nome)

    def salario_func(self):
        print(self.salario)

    def aumenta_salario(self, aumento):
        acrec = (self.salario * aumento) / 100
        self.salario = acrec + self.salario
        print(f'{self.nome} teve um aumento de {aumento}% no seu salario, agora ele ganha: R$ {self.salario}')



func1 = Funcionario('Astolfo', 1500.00)
func2 = Funcionario('Rubens', 500)

func1.nome_func()
func1.salario_func()
print('++++++++++++++++++++++')
func2.salario_func()
func2.aumenta_salario(15)