from limite.TelaCachorro import TelaCachorro
from entidade.Cachorro import Cachorro
from DAOs.CachorroDAO import CachorroDAO


class ControladorCachorro:

    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__cachorros = [] # type: ignore
        self.__tela_cachorro = TelaCachorro()
        self.__cachorro_DAO = CachorroDAO()
        try:
            self.__cachorros = list(self.__cachorro_DAO.get_all())
        except:
            pass

    def incluir_cachorro(self):
        dados_cachorro = self.__tela_cachorro.pega_dados_cachorro()
        novo_cachorro = Cachorro(dados_cachorro['numero_chip'], 
                         dados_cachorro['nome'],
                         dados_cachorro['raca'],
                         dados_cachorro['tamanho'])
        self.__cachorros.append(novo_cachorro)
        self.__cachorro_DAO.add(novo_cachorro)
        return novo_cachorro
    
    def alterar_cachorro(self):
        numero_cachorro = self.lista_cachorros(seleciona=True)
        cachorro = self.pega_cachorro_por_numero(numero_cachorro)

        if cachorro is not None:
            novos_dados = self.__tela_cachorro.pega_dados_cachorro()
            cachorro.numero_chip = novos_dados['numero_chip']
            cachorro.nome = novos_dados['nome']
            cachorro.raca = novos_dados['raca']
            cachorro.tamanho = novos_dados['tamanho']
        else:
            self.__tela_cachorro.mostra_mensagem('ATENÇÃO: cachorro não existente')
        self.lista_cachorros()

    def lista_cachorros(self, seleciona=False):
        lista_dados = []
        for cachorro in self.__cachorros:
            dados = {'numero_chip': cachorro.numero_chip,
                     'nome': cachorro.nome,
                     'raca': cachorro.raca,
                     'tamanho': cachorro.tamanho}
            lista_dados.append(dados)
        
        return self.__tela_cachorro.mostra_todos_cachorros(lista_dados, seleciona)

    def excluir_cachorro(self):
        numero_cachorro = self.lista_cachorros(seleciona=True)
        cachorro = self.pega_cachorro_por_numero(numero_cachorro)

        if cachorro is not None:
            self.__cachorros.remove(cachorro)
        else:
            self.__tela_cachorro.mostra_mensagem('ATENÇÃO: cachorro não existente')
        
        self.lista_cachorros()

    def pega_cachorro_por_numero(self, numero_cachorro):
        for cachorro in self.__cachorros:
            if cachorro.numero_chip == numero_cachorro:
                return cachorro
        return None

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