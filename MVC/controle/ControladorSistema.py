from controle.ControladorAnimal import ControladorAnimal
from limite.TelaSistema import TelaSistema


class ControladorSistema:
    def __init__(self) -> None:
        self.__adocoes = [] # type: ignore
        self.__doacoes = [] # type: ignore
        self.__pessoas = [] # type: ignore
        self.__tela_sistema = TelaSistema()
        self.__controlador_animais = ControladorAnimal(self)
    
    def inicializa_sistema(self):
        self.abre_tela()
    
    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        # Precisa completar
        lista_opcoes = {1: self.cadastrar_animal, 2: self.cadastrar_pessoa, 3: self.cadastrar_adocao,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def cadastrar_animal(self):
        self.__controlador_animais.abre_tela()

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