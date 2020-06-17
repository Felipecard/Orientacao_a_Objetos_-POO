
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):                                              # __str_- é a representacao textual daquele obejto
        return f'{self._nome} - {self.ano} - {self._likes} Likes'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)                  # super() - Chama qualquer metodo da classe mãe
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min -  {self._likes} Likes'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas -  {self._likes} Likes'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)





# MAIN:
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tep = Filme('Todo mundo em panico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_likes()
tep.dar_likes()
tep.dar_likes()
tep.dar_likes()
tep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

filmes_e_series = [vingadores, atlanta, demolidor, tep]

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho do Playlist: {len(playlist_fim_de_semana)}')

print(f'Demilidor esta dentro da playlist? {demolidor in playlist_fim_de_semana}')

for programa in playlist_fim_de_semana:
    print(programa)                # Aqui funciona o Polimorfismo.. Ele vai imprimir a class q tem o metodo imprimir
                                    # Qd for a hora do filme ou quando for a ahora da serie, NAO IMPORTA QUAL A CLASSE DO OBJETO

                                    # Polimorfismo != Duck Typing (Fazer um objeto se passar por outro, sem precisar fazer heranca)
