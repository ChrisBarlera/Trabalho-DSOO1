from abc import ABC, abstractmethod
from entidade.Vacinacao import Vacina, Vacinacao
from datetime import date as Date


class Animal(ABC):

    @abstractmethod
    def __init__(self, numero_chip: int, nome: str, raca: str):
        self.__numero_chip = None
        self.__nome = None
        self.__raca = None
        self.__vacinacoes = [] # type: list[Vacinacao]

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

    def vacinar(self, data: Date, vacina: Vacina) -> Vacinacao:
        if isinstance(data, Date) and isinstance(vacina, Vacina):
            nova_vacinacao = Vacinacao(data, self, vacina)
            self.__vacinacoes.append(nova_vacinacao)
            return nova_vacinacao
        else:
            print('Tipo inválido')
            return None
