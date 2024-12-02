# from enum import Enum

# class str(Enum):
#     CASA = 'casa',
#     APARTAMENTO = 'apartamento'

# class str(Enum):
#     PEQUENO = 1,
#     MEDIO = 2,
#     GRANDE = 3

class Habitacao:
    def __init__(self, numero: int, tipo: int, tamanho: int) -> None:
        self.__numero = None
        self.__tipo = None
        self.__tamanho = None

        ### Testando tipos das variáveis
        if isinstance(numero, int):
            self.__numero = numero
        else:
            print('Tipo inválido')

        if isinstance(tipo, int):
            self.__tipo = tipo
        else:
            print('Tipo inválido')
        
        if isinstance(tamanho, int):
            self.__tamanho = tamanho
        else:
            print('Tipo inválido')

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero: int):
        if isinstance(numero, int):
            self.__numero = numero
        else:
            print('Valor inválido. O valor deve ser um int')
    
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo: int):
        if isinstance(tipo, int):
            self.__tipo = tipo
        else:
            print('Valor inválido. O valor deve ser um int')

    @property
    def tamanho(self):
        return self.__tamanho
    
    @tamanho.setter
    def tamanho(self, tamanho: int):
        if isinstance(tamanho, int):
            self.__tamanho = tamanho
        else:
            print('Valor inválido. O valor deve ser um int')