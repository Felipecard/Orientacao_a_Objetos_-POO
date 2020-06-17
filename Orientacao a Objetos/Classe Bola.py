

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, cor_trocada):
        self.cor = cor_trocada

    def mostra_carac(self):
        print(f'A cor da bola ficou: {self.cor}')
        print(f'A circunferencia da bola ficou: {self.circunferencia}')
        print(f'O material da bola ficou: {self.material}')



# MAIN
bola1 = Bola('Azul', 10, 'ferro')

bola1.mostra_carac()
print('----------------------')
bola1.troca_cor('amarelo')
bola1.mostra_carac()

