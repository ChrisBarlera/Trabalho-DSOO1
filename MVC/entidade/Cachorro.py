from entidade.Animal import Animal
from enum import Enum


class Tamanho_Cachorro(Enum):
    PEQUENO = 1,
    MEDIO = 2,
    GRANDE = 3

class Cachorro(Animal):
    def __init__(self, numero_chip: int, nome: str, raca: str, tamanho: Tamanho_Cachorro):
        super().__init__(numero_chip, nome, raca)
        self.__tamanho = None

        if isinstance(tamanho, Tamanho_Cachorro):
            self.__tamanho = tamanho
        else:
            print('Tipo inválido')