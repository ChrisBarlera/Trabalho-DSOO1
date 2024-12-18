from entidade.Animal import Animal


class Gato(Animal):
    def __init__(self, numero_chip: int, nome: str, raca: str):
        super().__init__(numero_chip, nome, raca)
        self.__especie = 'Gato'

    @property
    def especie(self):
        return self.__especie
