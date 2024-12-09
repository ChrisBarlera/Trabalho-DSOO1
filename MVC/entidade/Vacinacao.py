from datetime import date as Date


class Vacinacao:
    def __init__(self, data: Date, animal, vacina: str, contador_id: int):
        self.__data = None
        self.__animal = animal
        self.__vacina = None
        self.__contador_id = contador_id

        ### Testando tipos das variáveis
        if isinstance(data, Date):
            self.__data = data
        else:
            print('Tipo inválido')

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
            print('Valor inválido. O valor deve ser um Date')

    @property
    def animal(self):
        return self.__animal
    
    @animal.setter
    def animal(self, animal):
        self.__animal = animal

    @property
    def vacina(self):
        return self.__vacina
    
    @vacina.setter
    def vacina(self, vacina: str):
        if isinstance(vacina, str):
            self.__vacina = vacina
        else:
            print('Valor inválido. O valor deve ser um str')

    @property
    def contador_id(self):
        return self.__contador_id
