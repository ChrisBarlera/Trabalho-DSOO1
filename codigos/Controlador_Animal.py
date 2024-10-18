from Animal import Animal
from codigos.Controlador_Sistema import Controlador_Sistema
from codigos.TelaAnimal import TelaAnimal


class Controlador_Animal:

    def __init__(self, controlador_sistema: Controlador_Sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__animais = [] # type: list[Animal]
        self.__tela_animal = TelaAnimal()