from MVC.limite.TelaAnimal import TelaAnimal
from MVC.controle.Controlador_Sistema import Controlador_Sistema


class Controlador_Animal:

    def __init__(self, controlador_sistema: Controlador_Sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__animais = [] # type: ignore
        self.__tela_animal = TelaAnimal()