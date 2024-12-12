from abc import ABC, abstractmethod
from datetime import date as Date


class Animal(ABC):

    @abstractmethod
    def __init__(self, numero_chip: int, nome: str, raca: str):
        self.__numero_chip = None
        self.__nome = None
        self.__raca = None
        self.__vacinacoes = [] # type: ignore

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

    @property
    @abstractmethod
    def especie(self):
        pass

    def remover_vacina_por_codigo(self, codigo):
        for vacina in self.__vacinacoes:
            if vacina.codigo == codigo:
                self.__vacinacoes.remove(vacina)
                break

    @property
    def numero_chip(self):
        return self.__numero_chip
    
    @numero_chip.setter
    def numero_chip(self, numero_chip: int):
        if isinstance(numero_chip, int):
            self.__numero_chip = numero_chip
        else:
            print("Valor inválido. O valor deve ser um int")

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            print("Valor inválido. O valor deve ser um str")
    
    @property
    def raca(self):
        return self.__raca
    
    @raca.setter
    def raca(self, raca: str):
        if isinstance(raca, str):
            self.__raca = raca
        else:
            print("Valor inválido. O valor deve ser um str")

    @property
    def vacinacoes(self):
        return self.__vacinacoes
    
    @vacinacoes.setter
    def vacinacoes(self, vacinacoes: list):
        if isinstance(vacinacoes, list):
            self.__vacinacoes = vacinacoes
        else:
            print("Valor inválido. O valor deve ser um list")
