from datetime import date as Date
from entidade.Adotante import Adotante
from entidade.Animal import Animal


class Adocao:
    def __init__(self, numero_id: int, adotante: Adotante, animal: Animal, data: Date):
        self.__adotante = None
        self.__animal = None
        self.__data = None
        self.__numero_id = None

        ### Testando tipos das variáveis
        if isinstance(numero_id, int):
            self.__numero_id = numero_id
        else:
            print('Tipo inválido')
    
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
    def numero_id(self):
        return self.__numero_id
    
    @numero_id.setter
    def numero_id(self, numero_id: int):
        if isinstance(numero_id, int):
            self.__numero_id = numero_id
        else:
            print('Valor inválido. O valor deve ser um int')
    
    @property
    def adotante(self):
        return self.__adotante
    
    @adotante.setter
    def adotante(self, adotante: Adotante):
        if isinstance(adotante, Adotante):
            self.__adotante = adotante
        else:
            print('Valor inválido. O valor deve ser um Adotante')
    
    @property
    def animal(self):
        return self.__animal
    
    @animal.setter
    def animal(self, animal: Animal):
        if isinstance(animal, Animal):
            self.__animal = animal
        else:
            print('Valor inválido. O valor deve ser um Animal')
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data: Date):
        if isinstance(data, Date):
            self.__data = data
        else:
            print('Valor inválido. O valor deve ser um Date')
