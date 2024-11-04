from datetime import date as Date
# from enum import Enum

# class Vacina(Enum):
#     RAIVA = 'raiva',
#     LEPTOSPIROSE = 'leptospirose',
#     HEPATITE_INFECCIOSA = 'hepatite infecciosa'

class Vacinacao:
    # def __init__(self, data: Date, animal: Animal, vacina: str) -> None:
    def __init__(self, data: Date, animal, vacina: str) -> None:
        self.__data = None
        self.__animal = animal
        self.__vacina = None

        ### Testando tipos das variáveis
        if isinstance(data, Date):
            self.__data = data
        else:
            print('Tipo inválido')
        
        # if isinstance(animal, Animal):
        #     self.__animal = animal
        # else:
        #     print('Tipo inválido')

        if isinstance(vacina, str):
            self.__vacina = vacina
        else:
            print('Tipo inválido')

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data: Date):
        if isinstance(data, Date):
            self.__data = data
        else:
            print("Valor inválido. O valor deve ser um Date")

    @property
    def animal(self):
        return self.__animal
    
    # @animal.setter
    # def animal(self, animal: Animal):
    #     if isinstance(animal, Animal):
    #         self.__animal = animal
    #     else:
    #         print("Valor inválido. O valor deve ser um Animal")

    @property
    def vacina(self):
        return self.__vacina
    
    @vacina.setter
    def vacina(self, vacina: str):
        if isinstance(vacina, str):
            self.__vacina = vacina
        else:
            print("Valor inválido. O valor deve ser um str")