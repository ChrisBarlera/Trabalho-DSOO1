from limite.TelaAnimal import TelaAnimal
from controle.ControladorGato import ControladorGato


class ControladorAnimal:

    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__controlador_gato = ControladorGato(controlador_sistema, )
        self.__animais = [] # type: ignore
        self.__tela_animal = TelaAnimal()

    def incluir_animal(self):
        dados_animal = self.__tela_animal.pega_dados_animal()
    
    def alterar_animal(self):
        pass

    def lista_animal(self):
        pass

    def excluir_animal(self):
        pass

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_animal, 2: self.alterar_animal, 3: self.lista_animal, 4: self.excluir_animal, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_animal.tela_opcoes()]()
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()