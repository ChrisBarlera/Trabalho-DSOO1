from datetime import date as Date


class Vacinacao:
    def __init__(self, codigo: int, data: Date, vacina: str):
        self.__codigo = None
        self.__data = None
        self.__vacina = None

        ### Testando tipos das variáveis
        if isinstance(codigo, int):
            self.__codigo = codigo
        else:
            print('Tipo inválido')

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
    def vacina(self):
        return self.__vacina
    
    @vacina.setter
    def vacina(self, vacina: str):
        if isinstance(vacina, str):
            self.__vacina = vacina
        else:
            print('Valor inválido. O valor deve ser um str')

    @property
    def codigo(self):
        return self.__codigo
