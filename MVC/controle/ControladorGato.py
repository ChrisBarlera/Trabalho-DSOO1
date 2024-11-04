from limite.TelaGato import TelaGato
from entidade.Gato import Gato


class ControladorGato:

    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__gatos = [] # type: ignore
        self.__tela_gato = TelaGato()

    def incluir_gato(self):
        dados_gato = self.__tela_gato.pega_dados_gato()
        novo_gato = Gato(dados_gato['numero_chip'], 
                         dados_gato['nome'],
                         dados_gato['raca'])
        self.__gatos.append(novo_gato)
        return novo_gato
    
    def alterar_gato(self):
        self.lista_gatos()
        numero_gato = self.__tela_gato.seleciona_gato()
        gato = self.pega_gato_por_numero(numero_gato)

        if gato is not None:
            novos_dados = self.__tela_gato.pega_dados_gato()
            gato.numero_chip = novos_dados['numero_chip']
            gato.nome = novos_dados['nome']
            gato.raca = novos_dados['raca']
        else:
            self.__tela_gato.mostra_mensagem('ATENCAO: Gato não existente')
        self.lista_gatos()

    def lista_gatos(self):
        for gato in self.__gatos:
            dados = {'numero_chip': gato.numero_chip,
                     'nome': gato.nome,
                     'raca': gato.raca}
            self.__tela_gato.mostra_gato(dados)

    def excluir_gato(self):
        self.lista_gatos()
        numero_gato = self.__tela_gato.seleciona_gato()
        gato = self.pega_gato_por_numero(numero_gato)

        if gato is not None:
            self.__gatos.remove(gato)
        else:
            self.__tela_gato.mostra_mensagem('ATENCAO: gato não existente')
        
        self.lista_gatos()

    def pega_gato_por_numero(self, numero_gato):
        for gato in self.__gatos:
            if gato.numero_chip == numero_gato:
                return gato
        return None

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_gato,
                        2: self.alterar_gato,
                        3: self.lista_gato,
                        4: self.excluir_gato,
                        0: self.retornar}

        while True:
            lista_opcoes[self.__tela_gato.tela_opcoes()]()
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()