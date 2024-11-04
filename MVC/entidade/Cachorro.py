from entidade.Animal import Animal
from enum import Enum


# class Tamanho_Cachorro(Enum):
#     PEQUENO = 1,
#     MEDIO = 2,
#     GRANDE = 3

class Cachorro(Animal):
    def __init__(self, numero_chip: int, nome: str, raca: str, tamanho: int):
    # def __init__(self, numero_chip: int, nome: str, raca: str, tamanho: Tamanho_Cachorro):
        super().__init__(numero_chip, nome, raca)
        self.__tamanho = None

        if isinstance(tamanho, int):
            self.__tamanho = tamanho
        else:
            print('Tipo inválido')

        # if isinstance(tamanho, Tamanho_Cachorro):
        #     self.__tamanho = tamanho
        # else:
        #     print('Tipo inválido')
        
        self.__especie = 'CACHORRO'

    @property
    def especie(self):
        return self.__especie
    
    @property
    def tamanho(self):
        return self.__tamanho
    
    # @tamanho.setter
    # def tamanho(self, tamanho: Tamanho_Cachorro):
    #     if isinstance(tamanho, Tamanho_Cachorro):
    #         self.__tamanho = tamanho
    #     else:
    #         print('Valor inválido. O valor deve ser um Tamanho_Cachorro')

    @tamanho.setter
    def tamanho(self, tamanho: int):
        if isinstance(tamanho, int):
            self.__tamanho = tamanho
        else:
            print('Valor inválido. O valor deve ser um int')
