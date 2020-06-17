
class Carro:
    def __init__(self, capacidade, qt_gasolina=0):
        self.capacidade = capacidade
        self.qt_gasolina= qt_gasolina
        self.km_rodados = 0

    def andar(self, km_rodados):
        pode_andar = self.qt_gasolina * self.capacidade
        self.km_rodados = km_rodados
        if pode_andar > km_rodados:
            print(f'O carro andou {km_rodados} Km e a ainda aguentaria andar mais {pode_andar - km_rodados} Km')
            return km_rodados
        else:
            print(f'O carro irá enguicar por falta de combustível, coloque mais gasolina!')

    def nivel_atual_gasolina(self):
        gasto_gasolina = self.km_rodados / self.capacidade
        nivel_atual = self.qt_gasolina - gasto_gasolina
        print(f'O carro ainda tem {nivel_atual} L de gasolina')

    def adicionar_gasolina(self, qt_gasolina):
        self.qt_gasolina = qt_gasolina


# OBJ:
fusca = Carro(8)
prisma = Carro(16)

# MAIN:
fusca.adicionar_gasolina(15)
fusca.andar(80)
fusca.nivel_atual_gasolina()
print('------------------------')