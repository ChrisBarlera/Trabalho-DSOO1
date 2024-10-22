from enum import Enum

class Tipo_Habitação(Enum):
    CASA = 'casa',
    APARTAMENTO = 'apartamento'

class Tamanho_Habitacao(Enum):
    PEQUENO = 1,
    MEDIO = 2,
    GRANDE = 3

class Habitacao:
    def __init__(self, tipo: Tipo_Habitação, tamanho: Tamanho_Habitacao) -> None:
        self.__tipo = None
        self.__tamanho = None

        ### Testando tipos das variáveis
        if isinstance(tipo, Tipo_Habitação):
            self.__tipo = tipo
        else:
            print('Tipo inválido')
        
        if isinstance(tamanho, Tamanho_Habitacao):
            self.__tamanho = tamanho
        else:
            print('Tipo inválido')

    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo: Tipo_Habitação):
        if isinstance(tipo, Tipo_Habitação):
            self.__tipo = tipo
        else:
            print("Valor inválido. O valor deve ser um Tipo_Habitação")

    @property
    def tamanho(self):
        return self.__tamanho
    
    @tamanho.setter
    def tamanho(self, tamanho: Tamanho_Habitacao):
        if isinstance(tamanho, Tamanho_Habitacao):
            self.__tamanho = tamanho
        else:
            print("Valor inválido. O valor deve ser um Tamanho_Habitacao")