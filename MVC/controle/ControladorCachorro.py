from limite.TelaCachorro import TelaCachorro
from entidade.Cachorro import Cachorro


class ControladorCachorro:

    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__cachorros = [] # type: ignore
        self.__tela_cachorro = TelaCachorro()

    def incluir_cachorro(self):
        dados_cachorro = self.__tela_cachorro.pega_dados_cachorro()
        novo_cachorro = Cachorro(dados_cachorro['numero_chip'], 
                         dados_cachorro['nome'],
                         dados_cachorro['raca'],
                         dados_cachorro['tamanho'])
        self.__cachorros.append(novo_cachorro)
        return novo_cachorro
    
    def alterar_cachorro(self):
        self.lista_cachorros()
        numero_cachorro = self.__tela_cachorro.seleciona_cachorro()
        cachorro = self.pega_cachorro_por_numero(numero_cachorro)

        if cachorro is not None:
            novos_dados = self.__tela_cachorro.pega_dados_cachorro()
            cachorro.numero_chip = novos_dados['numero_chip']
            cachorro.nome = novos_dados['nome']
            cachorro.raca = novos_dados['raca']
        else:
            self.__tela_cachorro.mostra_mensagem('ATENCAO: cachorro não existente')
        self.lista_cachorros()

    def lista_cachorros(self):
        for cachorro in self.__cachorros:
            dados = {'numero_chip': cachorro.numero_chip,
                     'nome': cachorro.nome,
                     'raca': cachorro.raca,
                     'tamanho': cachorro.tamanho}
            self.__tela_cachorro.mostra_cachorro(dados)

    def excluir_cachorro(self):
        self.lista_cachorros()
        numero_cachorro = self.__tela_cachorro.seleciona_cachorro()
        cachorro = self.pega_cachorro_por_numero(numero_cachorro)

        if cachorro is not None:
            self.__cachorros.remove(cachorro)
        else:
            self.__tela_cachorro.mostra_mensagem('ATENCAO: cachorro não existente')
        
        self.lista_cachorros()

    def pega_cachorro_por_numero(self, numero_cachorro):
        for cachorro in self.__cachorros:
            if cachorro.numero_chip == numero_cachorro:
                return cachorro
        return None

    def seleciona_cachorro(self):
        self.lista_cachorros()
        numero_cachorro =  self.__tela_cachorro.seleciona_cachorro()
        cachorro = self.pega_cachorro_por_numero(numero_cachorro)
        return cachorro

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_cachorro,
                        2: self.alterar_cachorro,
                        3: self.lista_cachorro,
                        4: self.excluir_cachorro,
                        0: self.retornar}

        while True:
            lista_opcoes[self.__tela_cachorro.tela_opcoes()]()
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()