from abc import ABC, abstractmethod
from vacinacao import Vacinacao

class Animal(ABC):
    
    @abstractmethod
    def __init__(self, numero_chip: int, nome: str, raca: str):
        self.__numero_chip = None
        self.__nome = None
        self.__raca = None

        ### Testando tipos das variáveis
        if isinstance(numero_chip, int):
            self.__numero_chip = numero_chip
        else:
            print('Tipo inválido')
        
        if isinstance(nome, str):
            self.__nome = nome
        else:
            print('Tipo inválido')

        if isinstance(raca, str):
            self.__raca = raca
        else:
            print('Tipo inválido')
    
    '''
    
    @return 
    '''
    def vacinar(self) -> Vacinacao:
        nova_vacinacao = Vacinacao()
        return nova_vacinacao

    '''
    
    @return
    '''
    @property
    @abstractmethod
    def numero_chip(self):
        return self.__numero_chip
    
    @numero_chip.setter
    def numero_chip(self, numero_chip: int):
        if isinstance(numero_chip, int):
            self.__numero_chip = numero_chip
        else:
            print("Valor inválido. O valor deve ser um int")

    '''
    
    @return
    '''
    @property
    @abstractmethod
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            print("Valor inválido. O valor deve ser um str")
    
    '''
    
    @return
    '''
    @property
    @abstractmethod
    def raca(self):
        return self.__raca
    
    @raca.setter
    def raca(self, raca: str):
        if isinstance(raca, str):
            self.__raca = raca
        else:
            print("Valor inválido. O valor deve ser um str")