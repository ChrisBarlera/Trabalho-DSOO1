from Controlador_Animal import Controlador_Animal


class Controlador_Sistema:
    def __init__(self) -> None:
        self.__adocoes = [] # type: ignore
        self.__doacoes = [] # type: ignore
        self.__pessoas = [] # type: ignore
        self.__controlador_animais = Controlador_Animal(self)
    
    def cadastrar_animal(self):
        pass

    def cadastrar_pessoa(self):
        pass

    def cadastrar_doacao(self):
        pass

    def cadastrar_adocao(self):
        pass

    def alterar_animal(self):
        pass

    def alterar_pessoa(self):
        pass

    def alterar_doacao(self):
        pass

    def alterar_adocao(self):
        pass

    def exluir_animal(self):
        pass

    def exluir_pessoa(self):
        pass

    def exluir_doacao(self):
        pass

    def exluir_adocao(self):
        pass