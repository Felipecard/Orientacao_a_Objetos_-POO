
class TV:
    def __init__(self, canal=0, volume=0):
        self.canal = canal
        self.volume = volume

    def mudar_volume(self):
        if vol < 0 or vol > 30:
            return print('O volume não pode ser aumentado ou diminuido mais que isso')
        else:
            self.volume = vol
            return self.volume

    def mudar_canal(self):
        if vol < 0 or vol > 100:
            return print('Os canais vai apenas ate o 100')
        else:
            self.canal = can
            return self.canal



vol = int(input('Para qual volume gostaria? '))
can = int(input('Para qual canal gostaria? '))
tv1 = TV(vol)


print(f'O VOLUME selecionado foi {tv1.mudar_volume()}')

print(f'O CANAL selecionado foi {tv1.mudar_canal()}')