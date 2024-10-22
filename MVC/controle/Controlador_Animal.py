from limite.TelaAnimal import TelaAnimal


class Controlador_Animal:

    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__animais = [] # type: ignore
        self.__tela_animal = TelaAnimal()