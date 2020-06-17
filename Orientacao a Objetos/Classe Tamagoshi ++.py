class Tamagoshi:
    def __init__(self, nome, idade, fome, saude):
        self.nome = nome
        self.idade = idade
        self.fome = fome
        self.saude = saude

    def altera_nome(self, nome):
        self.nome = nome
        print(f'O nome foi modificado para: {self.nome}')

    def aniversario(self, rodada):
        self.idade = rodada
        print(f'{self.nome} tem {self.idade} anos')


    def apetite(self, comida):
        if comida == 'melancia':
            self.fome = 'cheio'
        if comida == 'uva':
            self.fome = 'satisfeito'
        if comida == 'nada':
            self.fome = 'faminto'
        return print(f'Está {self.fome}')

    def cond_medica(self, fome, remedio):
        self.saude = remedio


        if  self.saude == 's':
            self.saude = 'Saudavel'
            print(self.saude)
        if fome == 'faminto' or self.saude == 'n':
            self.saude = 'Doente'
            print(self.saude)


    def humor(self):
        if self.fome == 'fome' or self.saude == 'doente':
            print('MAU HUMOR')
        else:
            print('BOM HUMOR')

    def __str__(self):
        if self.nome == 'Felipe':
            return f'Dados secretos: {self.nome}, {self.idade}, {self.fome}, {self.saude} '
        else:
            return '----'


# OBJ:
bicho1 = Tamagoshi('Luan', 0, 'satisfeito', 'saudavel')
bicho2 = Tamagoshi('Lara', 0, 'faminto', 'doente')

# MAIN:
rodada = 0
while rodada <= 5:
    print(f'RODADA {rodada}')
    comida = str(input(f'o que pretende dar de comer ao {bicho1.nome}? [melancia, uva ou nada?]'))
    remedio = str(input('Ele precisa de remédio? (s) ou (n)'))
    bicho1.aniversario(rodada)
    bicho1.apetite(comida)
    bicho1.cond_medica(bicho1.fome, remedio)
    bicho1.humor()
    print(bicho1)
    print('----------------------')
    bicho2.aniversario(rodada)
    bicho2.apetite(comida)
    bicho2.cond_medica(bicho2.fome, remedio)
    bicho2.humor()
    print(bicho1)



    print('-=' * 30)
    rodada += 1

print(f'O {bicho1.nome} morreu de velhice!')