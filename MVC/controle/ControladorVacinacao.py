from limite.TelaVacinacao import TelaVacinacao
from entidade.Vacinacao import Vacinacao


class ControladorVacinacao:

    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__controlador_animal = controlador_sistema.controlador_animal
        self.__vacinacoes = [] # type: ignore
        self.__tela_vacinacao = TelaVacinacao()
        
    def incluir_vacinacao(self):
        if len(self.__controlador_animal.animais) != 0:
            animal = self.__controlador_animal.seleciona_animal()
        else:
            self.__tela_vacinacao.mostra_mensagem('Cadastre um animal')
            animal = self.__controlador_animal.incluir_animal()
        dados_vacinacao = self.__tela_vacinacao.pega_dados_vacinacao()
        nova_vacinacao = Vacinacao(dados_vacinacao['data'],
                                   animal,
                                   dados_vacinacao['vacina'])
        self.__vacinacoes.append(nova_vacinacao)
        return nova_vacinacao
    
    def alterar_vacinacao(self):
        vacinacao = self.seleciona_vacinacao()

        if vacinacao is not None:
            novos_dados = self.__tela_vacinacao.pega_dados_vacinacao()
            vacinacao.numero = novos_dados['numero']
            vacinacao.tipo = novos_dados['tipo']
            vacinacao.tamanho = novos_dados['tamanho']
        else:
            self.__tela_vacinacao.mostra_mensagem('ATENCAO: habitação não existente')
        self.lista_vacinacoes()

    def lista_vacinacoes(self):
        for vacinacao in self.__vacinacoes:
            dados = {'numero': vacinacao.numero,
                     'tipo': vacinacao.tipo,
                     'tamanho': vacinacao.tamanho}
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

    def seleciona_vacinacao(self):
        self.lista_vacinacoes()
        numero_vacinacao =  self.__tela_vacinacao.seleciona_vacinacao()
        vacinacao = self.pega_vacinacao_por_numero(numero_vacinacao)
        return vacinacao

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