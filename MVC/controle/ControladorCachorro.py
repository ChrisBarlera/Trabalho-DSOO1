from limite.TelaCachorro import TelaCachorro


class ControladorCachorro:

    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__cachorros = [] # type: ignore
        self.__tela_cachorro = TelaCachorro()

    def incluir_cachorro(self):
        dados_cachorro = self.__tela_cachorro.pega_dados_cachorro()
        
    
    def alterar_cachorro(self):
        pass

    def lista_cachorro(self):
        pass

    def excluir_cachorro(self):
        pass

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_cachorro, 2: self.alterar_cachorro, 3: self.lista_cachorro, 4: self.excluir_cachorro, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_cachorro.tela_opcoes()]()
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()