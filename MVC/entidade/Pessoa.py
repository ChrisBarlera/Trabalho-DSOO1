from abc import ABC, abstractmethod
from datetime import date as Date


class Pessoa(ABC):
    
    @abstractmethod
    def __init__(self, cpf: int, nome: str, data_nasc: Date, endereco: str):
        self.__cpf = None
        self.__nome = None
        self.__data_nasc = None
        self.__endereco = None

        ### Testando tipos das variáveis
        if isinstance(cpf, int):
            self.__cpf = cpf
        else:
            print('Tipo inválido')
        
        if isinstance(nome, str):
            self.__nome = nome
        else:
            print('Tipo inválido')

        if isinstance(data_nasc, Date):
            self.__data_nasc = data_nasc
        else:
            print('Tipo inválido')

        if isinstance(endereco, str):
            self.__endereco = endereco
        else:
            print('Tipo inválido')

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf: int):
        if isinstance(cpf, int):
            self.__cpf = cpf
        else:
            print('Valor inválido. O valor deve ser um int')
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            print('Valor inválido. O valor deve ser um str')
    
    @property
    def data_nasc(self):
        return self.__data_nasc
    
    @data_nasc.setter
    def data_nasc(self, data_nasc: Date):
        if isinstance(data_nasc, Date):
            self.__data_nasc = data_nasc
        else:
            print('Valor inválido. O valor deve ser um Date')

    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco: str):
        if isinstance(endereco, str):
            self.__endereco = endereco
        else:
            print('Valor inválido. O valor deve ser um str')
    
    def calcula_idade(self):
        hoje = Date.today()
        return (hoje - self.__data_nasc).days // 365 # type: ignore
