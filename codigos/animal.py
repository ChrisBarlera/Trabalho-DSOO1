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
    
    '''
    
    @return 
    '''
    def vacinar(self) -> Vacinacao:
        pass

    '''
    
    @return
    '''
    @property
    @abstractmethod
    def personagem(self) -> Personagem:
        pass