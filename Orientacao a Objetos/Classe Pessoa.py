
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        return print(f'A pessoa tem agora: {self.idade + anos} anos')

    def engordar(self, massa):
        return print(f'A pessoa engordou {massa}Kg e ficou com: {self.peso + massa} Kg')

    def emagrecer(self, massa):
        return print(f' {self.nome} emagreceu {massa}Kg e ficou com: {self.peso - massa} Kg')

    def crescer(self, anos):
        c = anos * 0.005
        if self.idade < 21:
            return print(f'A pessoa cresceu {c}cm e ficou com: {self.altura + c}m')
        else:
            return print(f'A pessoa nao cresceu  contnuou com: {self.altura}m')



  # MAIN
pessoa1 = Pessoa('Tereza', 4, 25, 0.60)

print('--------------------------------------------------------------------------')
anos = int(input('Quantos ano se passaram? '))
print(f'O ano analisado é {2020 + anos}')
pessoa1.envelhecer(anos)
print('--------------------------------------------------------------------------')

massa = int(input('A pessoa 1 perdeu ou ganhou quantos Kg? '))

if massa < 0:
    massa = massa * (-1)
    pessoa1.emagrecer(massa)
else:
    pessoa1.engordar(massa)

print('---------------------------------------------------------------------------')
pessoa1.crescer(anos)
