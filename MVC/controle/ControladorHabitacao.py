from limite.TelaHabitacao import TelaHabitacao
from entidade.Habitacao import Habitacao
from DAOs.HabitacaoDAO import HabitacaoDAO


class ControladorHabitacao:

    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__habitacoes = [] # type: ignore
        self.__tela_habitacao = TelaHabitacao()
        self.__habitacao_DAO = HabitacaoDAO()
        try:
            self.__habitacoes = list(self.__habitacao_DAO.get_all())
        except:
            pass
        
    def incluir_habitacao(self):
        dados_habitacao = self.__tela_habitacao.pega_dados_habitacao()
        nova_habitacao = Habitacao(dados_habitacao['numero'], 
                         dados_habitacao['tipo'],
                         dados_habitacao['tamanho'])
        self.__habitacoes.append(nova_habitacao)
        self.__habitacao_DAO.add(nova_habitacao)
        return nova_habitacao
    
    def alterar_habitacao(self):
        numero_hab = self.lista_habitacoes(seleciona=True)
        habitacao = self.pega_habitacao_por_numero(numero_hab)

        if habitacao is not None:
            self.__habitacao_DAO.remove(habitacao.numero)
            novos_dados = self.__tela_habitacao.pega_dados_habitacao()
            habitacao.numero = novos_dados['numero']
            habitacao.tipo = novos_dados['tipo']
            habitacao.tamanho = novos_dados['tamanho']
            self.__habitacao_DAO.add(habitacao)
        else:
            self.__tela_habitacao.mostra_mensagem('ATENÇÃO: habitação não existente')
        self.lista_habitacoes()

    def lista_habitacoes(self, seleciona=False):
        lista_dados = []
        for habitacao in self.__habitacoes:
            dados = {'numero': habitacao.numero,
                     'tipo': habitacao.tipo,
                     'tamanho': habitacao.tamanho}
            lista_dados.append(dados)
        return self.__tela_habitacao.mostra_todas_habitacoes(lista_dados, seleciona)

    def excluir_habitacao(self):
        self.lista_habitacoes()
        numero_habitacao = self.__tela_habitacao.seleciona_habitacao()
        habitacao = self.pega_habitacao_por_numero(numero_habitacao)

        if habitacao is not None:
            self.__habitacao_DAO.remove(habitacao.numero)
            self.__habitacoes.remove(habitacao)
        else:
            self.__tela_habitacao.mostra_mensagem('ATENÇÃO: habitacao não existente')
        
        self.lista_habitacoes()

    def pega_habitacao_por_numero(self, numero_habitacao):
        for habitacao in self.__habitacoes:
            if habitacao.numero == numero_habitacao:
                return habitacao
        return None

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_habitacao,
                        2: self.alterar_habitacao,
                        3: self.lista_habitacoes,
                        4: self.excluir_habitacao,
                        0: self.retornar}

        while True:
            lista_opcoes[self.__tela_habitacao.tela_opcoes()]()
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()