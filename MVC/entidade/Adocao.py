from datetime import date as Date
from entidade.Adotante import Adotante
from entidade.Animal import Animal


class Adocao:
    def __init__(self, adotante: Adotante, animal: Animal, data: Date) -> None:
        self.__adotante = None
        self.__animal = None
        self.__data = None

        ### Testando tipos das variáveis
        if isinstance(adotante, Adotante):
            self.__adotante = adotante
        else:
            print('Tipo inválido')
        
        if isinstance(animal, Animal):
            self.__animal = animal
        else:
            print('Tipo inválido')
    
        if isinstance(data, Date):
            self.__data = data
        else:
            print('Tipo inválido')

    @property
    def adotante(self):
        return self.__adotante
    
    @adotante.setter
    def adotante(self, adotante: Adotante):
        if isinstance(adotante, Adotante):
            self.__adotante = adotante
        else:
            print("Valor inválido. O valor deve ser um Adotante")
    
    @property
    def animal(self):
        return self.__animal
    
    @animal.setter
    def animal(self, animal: Animal):
        if isinstance(animal, Animal):
            self.__animal = animal
        else:
            print("Valor inválido. O valor deve ser um Animal")
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data: Date):
        if isinstance(data, Date):
            self.__data = data
        else:
            print("Valor inválido. O valor deve ser um Date")
