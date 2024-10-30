from limite.TelaGato import TelaGato


class ControladorGato:

    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__animais = [] # type: ignore
        self.__tela_gato = TelaGato()

    def incluir_gato(self):
        dados_gato = self.__tela_gato.pega_dados_gato()
    
    def alterar_gato(self):
        pass

    def lista_gato(self):
        pass

    def excluir_gato(self):
        pass

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_gato, 2: self.alterar_gato, 3: self.lista_gato, 4: self.excluir_gato, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_gato.tela_opcoes()]()
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()