
class Tamagoshi:
    def __init__(self, nome, idade, fome, saude):
        self.nome = nome
        self.idade = idade
        self.fome = fome
        self.saude = saude

    def altera_nome(self, nome):
        self.nome = nome

    def cumpleanos(self, rodadas):
        self.idade = rodadas

    def apetite(self, porcoes_comida, rodadas):
        if porcoes_comida == 0:
            self.fome = 'Faminto'
        elif porcoes_comida == 1 or porcoes_comida == 2:
            self.fome = 'Satisfeito'
        elif porcoes_comida > 2 and porcoes_comida < 7:
            self.fome = 'Cheio'
        elif porcoes_comida > 7:
            self.fome = 'Comeu MUITO, o estomago estourou!'

    def cond_medica(self, rodadas, remedio):
            if rodadas < 8 or rodadas < 16:
                self.saude = 'Saudável'
            else:
                if remedio == True:
                    self.saude = 'Saudável'
                else:
                    self.saude = 'Doente'



# OBJ:
bicho1 = Tamagoshi('Cesar', 0, 'Faminto', 'Saudavel')

# MAIN
bicho1.altera_nome('Cesinha')
print(f'O novo nome é: {bicho1.nome} ')
print()

rodadas = 0
f = 0
while rodadas <= 60:
    print('-----------------------------------------------------------------------------------------')
    bicho1.cumpleanos(rodadas)
    print(f'Se passaram {rodadas} rodadas e o {bicho1.nome} esta com {bicho1.idade} dias de vida')

    porcoes_comida = int(input(f'Quantas porcões de arroz deseja dar para {bicho1.nome}?'))
    bicho1.apetite(porcoes_comida, rodadas)
    print(f'{bicho1.nome} comeu {porcoes_comida} porcão(s) de arroz e está {bicho1.fome}')

    if bicho1.fome == 'Faminto':
        f += 1
    if f == 3:
        rodadas = 61
    if bicho1.fome == 'Comeu MUITO, o estomago estourou!':
        rodadas = 61

    remedio = False
    bicho1.cond_medica(rodadas, remedio)
    print(f'{bicho1.nome} está {bicho1.saude}')

    if bicho1.fome == 'Satisfeito' and bicho1.saude == 'Saudável':
        print(f'{bicho1.nome} está FELIZ!')
    else:
        print(f'{bicho1.nome} está TRISTE!')

    print('-----------------------------------------------------------------------------------------')
    rodadas += 1

print(f'{bicho1.nome} MORREU! :(')

