from entidade.Animal import Animal
# from enum import Enum
# class Tamanho_Cachorro(Enum):
#     PEQUENO = 1,
#     MEDIO = 2,
#     GRANDE = 3

class Cachorro(Animal):
    def __init__(self, numero_chip: int, nome: str, raca: str, tamanho: str):
        super().__init__(numero_chip, nome, raca)
        self.__tamanho = None

        if isinstance(tamanho, str):
            self.__tamanho = tamanho
        else:
            print('Tipo inválido')
    
    @property
    def tamanho(self):
        return self.__tamanho
    
    @tamanho.setter
    def tamanho(self, tamanho: str):
        if isinstance(tamanho, str):
            self.__tamanho = tamanho
        else:
            print("Valor inválido. O valor deve ser um str")
