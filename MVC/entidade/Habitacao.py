class Habitacao:
    def __init__(self, numero: int, tipo: str, tamanho: str) -> None:
        self.__numero = numero
        self.__tipo = tipo
        self.__tamanho = tamanho

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero: int):
        self.__numero = numero
    
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo: str):
        self.__tipo = tipo

    @property
    def tamanho(self):
        return self.__tamanho
    
    @tamanho.setter
    def tamanho(self, tamanho: str):
        self.__tamanho = tamanho