from limite.TelaVacinacao import TelaVacinacao
from entidade.Vacinacao import Vacinacao
from DAOs.VacinacaoDAO import VacinacaoDAO


class ControladorVacinacao:

    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__controlador_animal = controlador_sistema.controlador_animal
        self.__vacinacoes = [] # type: ignore
        self.__tela_vacinacao = TelaVacinacao()
        self.__contador_id_vac = 0
        self.__vacinacao_DAO = VacinacaoDAO()
        
    def incluir_vacinacao(self):
        if not self.ja_tem_animal():
            return
        animal = self.__controlador_animal.seleciona_animal()
        dados_vacinacao = self.__tela_vacinacao.pega_dados_vacinacao()
        nova_vacinacao = Vacinacao(dados_vacinacao['data'],
                                   animal,
                                   dados_vacinacao['vacina'],
                                   self.__contador_id_vac)
        self.__contador_id_vac += 1
        self.__vacinacoes.append(nova_vacinacao)
        animal.vacinacoes.append(nova_vacinacao)
        self.__vacinacao_DAO.add(nova_vacinacao)
        return nova_vacinacao
    
    def alterar_vacinacao(self):
        vacinacao = self.seleciona_vacinacao()

        if vacinacao is not None:
            novos_dados = self.__tela_vacinacao.pega_dados_vacinacao()
            vacinacao.numero = novos_dados['numero']
            vacinacao.tipo = novos_dados['tipo']
            vacinacao.tamanho = novos_dados['tamanho']
        else:
            self.__tela_vacinacao.mostra_mensagem('ATENÇÃO: vacinação não existente')
        self.lista_vacinacoes()

    def lista_vacinacoes(self):
        animal = self.__controlador_animal.seleciona_animal()
        for vacinacao in animal.vacinacoes:
            dados = {
                'data': vacinacao.data,
                'vacina': vacinacao.vacina
            }
            self.__tela_vacinacao.mostra_vacinacao(dados)

    def excluir_vacinacao(self):
        self.lista_vacinacoes()
        numero_vacinacao = self.__tela_vacinacao.seleciona_vacinacao()
        vacinacao = self.pega_vacinacao_por_numero(numero_vacinacao)

        if vacinacao is not None:
            self.__vacinacoes.remove(vacinacao)
        else:
            self.__tela_vacinacao.mostra_mensagem('ATENÇÃO: vacinacao não existente')
        self.lista_vacinacoes()

    def pega_vacinacao_por_numero(self, numero_vacinacao):
        for vacinacao in self.__vacinacoes:
            if vacinacao.numero == numero_vacinacao:
                return vacinacao
        return None

    def ja_tem_animal(self):
        return self.__tela_vacinacao.ja_tem_animal()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_vacinacao,
                        2: self.alterar_vacinacao,
                        3: self.lista_vacinacoes,
                        4: self.excluir_vacinacao,
                        0: self.retornar}

        while True:
            lista_opcoes[self.__tela_vacinacao.tela_opcoes()]()
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()