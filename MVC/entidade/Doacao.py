from datetime import date as Date
from entidade.Doador import Doador
from entidade.Animal import Animal


class Doacao:
    def __init__(self, numero_id: int, doador: Doador,
                 animal: Animal, data: Date, motivo: str):
        self.__doador = None
        self.__animal = None
        self.__data = None
        self.__numero_id = None
        self.__motivo = None

        ### Testando tipos das variáveis
        if isinstance(numero_id, int):
            self.__numero_id = numero_id
        else:
            print('Tipo inválido')
    
        if isinstance(doador, Doador):
            self.__doador = doador
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
        
        if isinstance(motivo, str):
            self.__motivo = motivo
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
    def doador(self):
        return self.__doador
    
    @doador.setter
    def doador(self, doador: Doador):
        if isinstance(doador, Doador):
            self.__doador = doador
        else:
            print('Valor inválido. O valor deve ser um doador')
    
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

    @property
    def motivo(self):
        return self.__motivo
    
    @motivo.setter
    def motivo(self, motivo: str):
        if isinstance(motivo, str):
            self.__motivo = motivo
        else:
            print('Valor inválido. O valor deve ser um str')
