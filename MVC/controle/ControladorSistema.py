from controle.ControladorAnimal import ControladorAnimal
from controle.ControladorPessoa import ControladorPessoa
from limite.TelaSistema import TelaSistema


class ControladorSistema:
    def __init__(self) -> None:
        self.__adocoes = [] # type: ignore
        self.__doacoes = [] # type: ignore
        self.__pessoas = [] # type: ignore
        self.__tela_sistema = TelaSistema()
        self.__controlador_animais = ControladorAnimal(self)
        self.__controlador_pessoas = ControladorPessoa(self)
    
    def inicializa_sistema(self):
        self.abre_tela()
    
    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        # Precisa completar
        lista_opcoes = {1: self.acessar_animal,
                        2: self.acessar_pessoa,
                        3: self.acessar_adocao,
                        4: self.acessar_doacao,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def acessar_animal(self):
        self.__controlador_animais.abre_tela()

    def acessar_pessoa(self):
        self.__controlador_pessoas.abre_tela()

    def acessar_doacao(self):
        pass

    def acessar_adocao(self):
        pass
