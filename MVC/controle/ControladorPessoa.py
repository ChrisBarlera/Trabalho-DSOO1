from limite.TelaPessoa import TelaPessoa
from controle.ControladorDoador import ControladorDoador
from controle.ControladorAdotante import ControladorAdotante

class ControladorPessoa:

    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__controlador_doador = controlador_sistema.controlador_doador
        self.__controlador_adotante = controlador_sistema.controlador_adotante
        self.__pessoas = [] # type: ignore # E se eu fizer uma matriz Nx2?
        self.__tela_pessoa = TelaPessoa()

    def incluir_pessoa(self):
        opcao = self.__tela_pessoa.decide_tipo_pessoa()
        if opcao == 1:
            nova_pessoa = self.__controlador_doador.incluir_doador()
        else:
            nova_pessoa = self.__controlador_adotante.incluir_adotante()
        self.__pessoas.append(nova_pessoa)
    
    def alterar_pessoa(self):
        opcao = self.__tela_pessoa.decide_tipo_pessoa()
        if opcao == 1:
            self.__controlador_doador.alterar_doador()
        else:
            self.__controlador_adotante.alterar_adotante()

    def lista_pessoas(self):
        opcao = self.__tela_pessoa.decide_mostra_tipo()

        if opcao == 1:
            self.__controlador_doador.lista_doadores()
        elif opcao == 2:
            self.__controlador_adotante.lista_adotantes()
        else:
            # for Pessoa in self.__pessoas:
            #     if isinstance(Pessoa,Gato):
            #         self.__controlador_doador.lista_gatos()
            print(self.__pessoas) # placeholder
        

    def excluir_pessoa(self):
        opcao = self.__tela_pessoa.decide_tipo_pessoa()
        if opcao == 1:
            self.__controlador_doador.excluir_doador()
        else:
            self.__controlador_adotante.excluir_adotante()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_pessoa,
                        2: self.alterar_pessoa,
                        3: self.lista_pessoas,
                        4: self.excluir_pessoa,
                        0: self.retornar}

        while True:
            lista_opcoes[self.__tela_pessoa.tela_opcoes()]()
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()