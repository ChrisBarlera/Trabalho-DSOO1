from controle.ControladorGato import ControladorGato
from controle.ControladorCachorro import ControladorCachorro
from controle.ControladorAnimal import ControladorAnimal
from controle.ControladorPessoa import ControladorPessoa
from controle.ControladorDoador import ControladorDoador
from controle.ControladorAdotante import ControladorAdotante
from controle.ControladorAdocao import ControladorAdocao
from controle.ControladorDoacao import ControladorDoacao
from controle.ControladorHabitacao import ControladorHabitacao
from controle.ControladorVacinacao import ControladorVacinacao
from limite.TelaSistema import TelaSistema


class ControladorSistema:
    __instance = None

    def __init__(self) -> None:
        self.__adocoes = [] # type: ignore
        self.__doacoes = [] # type: ignore
        self.__pessoas = [] # type: ignore
        self.__tela_sistema = TelaSistema()
        self.__controlador_gato = ControladorGato(self)
        self.__controlador_cachorro = ControladorCachorro(self)
        self.__controlador_animal = ControladorAnimal(self)
        self.__controlador_vacinacao = ControladorVacinacao(self)
        self.__controlador_doador = ControladorDoador(self)
        self.__controlador_habitacao = ControladorHabitacao(self)
        self.__controlador_adotante = ControladorAdotante(self)
        self.__controlador_pessoa = ControladorPessoa(self)
        self.__controlador_doacao = ControladorDoacao(self)
        self.__controlador_adocao = ControladorAdocao(self)
    
    def __new__(cls):
        if ControladorSistema.__instance is None:
            ControladorSistema.__instance = object.__new__(cls)
        return ControladorSistema.__instance

    def inicializa_sistema(self):
        self.abre_tela()
    
    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.acessar_animal,
                        2: self.acessar_pessoa,
                        3: self.acessar_adocao,
                        4: self.acessar_doacao,
                        5: self.acessar_habitacao,
                        6: self.acessar_vacinacao,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def acessar_animal(self):
        self.__controlador_animal.abre_tela()

    def acessar_pessoa(self):
        self.__controlador_pessoa.abre_tela()

    def acessar_adocao(self):
        self.__controlador_adocao.abre_tela()
    
    def acessar_doacao(self):
        self.controlador_doacao.abre_tela()
    
    def acessar_habitacao(self):
        self.__controlador_habitacao.abre_tela()
    
    def acessar_vacinacao(self):
        self.__controlador_vacinacao.abre_tela()
    
    @property
    def controlador_gato(self):
        return self.__controlador_gato
    
    @property
    def controlador_cachorro(self):
        return self.__controlador_cachorro

    @property
    def controlador_animal(self):
        return self.__controlador_animal

    @property
    def controlador_pessoa(self):
        return self.__controlador_pessoa
    
    @property
    def controlador_doador(self):
        return self.__controlador_doador

    @property
    def controlador_adotante(self):
        return self.__controlador_adotante

    @property
    def controlador_adocao(self):
        return self.__controlador_adocao

    @property
    def controlador_doacao(self):
        return self.__controlador_doacao
    
    @property
    def controlador_habitacao(self):
        return self.__controlador_habitacao
    
    @property
    def controlador_vacinacao(self):
        return self.__controlador_vacinacao
