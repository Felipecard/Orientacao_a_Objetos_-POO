
class Urso:
    def __init__(self, nome, bucho):
        self.nome = nome
        self.bucho = bucho

    def comer(self, refeicao):
        self.bucho = refeicao

    def ver_bucho(self):
        satisfacao = self.bucho * 10
        if self.bucho == 1:
            comida = 'Bolinho'
        elif self.bucho == 2:
            comida = 'Salmão'
        elif self.bucho == 0:
            comida = 'Nada'
        return print(f'{self.nome} comeu {comida} e seu bucho está {satisfacao}% cheio')

    def digerir(self):
        self.bucho -= 1


def cabecalho():
    print('-=' * 25)
    print('            SALVANDO O ZÉ COLMEIA')
    print('-=' * 25)
    print('No inverno gelado da Sibéria, dois amigos ursos, Zé Colmeia e Puff, estão perdidos...')
    print('Puff resolveu hibernar, apostando que assim gastaria menos energia e consegruiria esperar o resgate sem comer!')
    print('Agora tente salvar Zé Colmeia...')
    print()
    print('A cada dia, o bucho Zé Colmeia digere 10% do que ele comeu!!!')
    print('Faca o Zé Colmeia sobreviver 5 dias, esse tempo é suficiente para o resgate chegar...')
    print('-=' * 30)
    print()
    print()


# OBJ:
urso1 = Urso('Zé Colmeia', 1)
urso2 = Urso('Puff', 0)

# MAIN
cabecalho()


dia = 1
m = 2
s = 1
while dia <= 5:
    print()
    print(f'DIA {dia}  ------------------------------------------------------------  DIA {dia}')
    vai = 100
    print(f'Estoque: Bolinho ({m}) | Salmão ({s})')
    if m > 0 or s > 0:
        while vai == 100:
            refeicao = int(input(f'O que o {urso1.nome} irá comer hoje? [1 - Bolinho (10%) | 2 - Salmão (20%)]'))
            if refeicao == 1:
                if m == 0:
                    print('Os Bolinhos acabaram, tente o Salmão!')
                    refeicao = int(input(f'O que o {urso1.nome} irá comer hoje? [1 - Bolinho (10%) | 2 - Salmão (20%)]'))
            elif refeicao == 2:
                if s == 0:
                    print('Os Bolinhos acabaram, tente o Bolinho!')
                    refeicao = int(input(f'O que o {urso1.nome} irá comer hoje? [1 - Bolinho (10%) | 2 - Salmão (20%)]'))
            vai = 50

        enigma = str(input(f'Será que {urso1.nome} teria algo mais para comer? Tente algum alimento...'))
    else:
        print('Os suprimentos acabaram e Zé Colmeia morreu!')
        break

    if refeicao == 1:
        m -= 1
    elif refeicao == 2:
        s -= 1

    if enigma == 'puff':
        print('Zé Colmeia cortou o Puff em pedacinhos e o comeu... Sem bucho ficou 500% cheio e ele sobreviveu.. PARABENS!!!')
        break
    else:
        print('Como ele encontraria isso no meio da Sibéria se no estoque dele não tem?!')
        print('***************')
    urso1.comer(refeicao)
    urso1.ver_bucho()


    if urso1.bucho == 0:
        print('O Zé Colmeia morreu de fome! GAME OVER!!!')
        break
    urso1.digerir()
    dia += 1
    refeicao = 0

if enigma != 'puff':
    print('O Dia 5 chegou e Zé Colmeia morreu de fome! GAME OVER!!!')