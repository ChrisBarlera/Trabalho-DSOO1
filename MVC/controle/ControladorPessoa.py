from limite.TelaPessoa import TelaPessoa
from controle.ControladorGato import ControladorGato
from entidade.Gato import Gato  #necessario para isInstance()
from entidade.Cachorro import Cachorro #necessario para isInstance()


class ControladorPessoa:

    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__controlador_gato = ControladorGato(controlador_sistema)
        # self.__controlador_cachorro = ControladorCachorro(controlador_sistema)
        self.__pessoas = [] # type: ignore # E se eu fizer uma matriz Nx2?
        self.__tela_pessoa = TelaPessoa()

    def incluir_pessoa(self):
        opcao = self.__tela_pessoa.decide_tipo_Pessoa()
        if opcao == 1:
            nova_pessoa = self.__controlador_gato.incluir_gato()
        else:
            # nova_pessoa = self.__controlador_cachorro.incluir_cachorro()
            pass
        self.__pessoas.append(nova_pessoa)
    
    def alterar_pessoa(self):
        opcao = self.__tela_pessoa.decide_tipo_Pessoa()
        if opcao == 1:
            self.__controlador_gato.alterar_gato()
        else:
            # self.__controlador_cachorro.alterar_cachorro()
            pass

    def lista_pessoas(self):
        opcao = self.__tela_pessoa.decide_mostra_tipo()

        if opcao == 1:
            self.__controlador_gato.lista_gatos() # placeholder
        elif opcao == 2:
            # print(self.__controlador_cachorro.__cachorros) # placeholder
            pass
        else:
            # for Pessoa in self.__pessoas:
            #     if isinstance(Pessoa,Gato):
            #         self.__controlador_gato.lista_gatos()
            print(self.__pessoas) # placeholder
        

    def excluir_pessoa(self):
        pass

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