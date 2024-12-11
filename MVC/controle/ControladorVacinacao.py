from limite.TelaVacinacao import TelaVacinacao
from entidade.Vacinacao import Vacinacao
from DAOs.VacinacaoDAO import VacinacaoDAO


class ControladorVacinacao:

    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__controlador_animal = controlador_sistema.controlador_animal
        self.__vacinacoes = [] # type: ignore
        self.__tela_vacinacao = TelaVacinacao()
        self.__contador_id_vac = 1
        self.__vacinacao_DAO = VacinacaoDAO()
        try:
            self.__vacinacoes = list(self.__vacinacao_DAO.get_all())
        except:
            pass
        
    def incluir_vacinacao(self):
        if not self.ja_tem_animal():
            return
        numero = self.__controlador_animal.lista_animais(seleciona=True)
        animal = self.__controlador_animal.pega_animal_por_numero(numero)
        dados_vacinacao = self.__tela_vacinacao.pega_dados_vacinacao()
        nova_vacinacao = Vacinacao(dados_vacinacao['data'],
                                   dados_vacinacao['vacina'],
                                   self.__contador_id_vac)
        self.__contador_id_vac += 1
        self.__vacinacoes.append(nova_vacinacao)
        animal.vacinacoes.append(nova_vacinacao)
        self.__vacinacao_DAO.add(nova_vacinacao)
        return nova_vacinacao
    
    def alterar_vacinacao(self):
        pass
        # numero_animal = self.__controlador_animal.lista_animais(seleciona=True)
        # animal = self.__controlador_animal.pega_animal_por_numero(numero_animal)

        # if animal is not None:
        #     novos_dados = self.__tela_vacinacao.pega_dados_vacinacao()
        #     vacinacao.numero = novos_dados['numero']
        #     vacinacao.tipo = novos_dados['tipo']
        #     vacinacao.tamanho = novos_dados['tamanho']
        # else:
        #     self.__tela_vacinacao.mostra_mensagem('ATENÇÃO: vacinação não existente')
        # self.lista_vacinacoes()

    def lista_vacinacoes(self, seleciona=False):
        lista_dados = []
        for vacinacao in self.__vacinacoes:
            dados = {'contador_id': vacinacao.contador_id,
                     'data': vacinacao.data,
                     'vacina': vacinacao.vacina,
                     'nome_animal': vacinacao.animal.nome}
            lista_dados.append(dados)
        return self.__tela_vacinacao.mostra_todas_vacinacoes(lista_dados, seleciona)

    def excluir_vacinacao(self):
        contador_id = self.lista_vacinacoes(seleciona=True)
        vacinacao = self.pega_vacinacao_por_numero(contador_id)

        if vacinacao is not None:
            self.__vacinacao_DAO.remove(vacinacao.contador_id)
            self.__vacinacoes.remove(vacinacao)
        else:
            self.__tela_vacinacao.mostra_mensagem('ATENÇÃO: vacinacao não existente')
        # self.lista_vacinacoes()

    def pega_vacinacao_por_numero(self, numero_vacinacao):
        for vacinacao in self.__vacinacoes:
            if vacinacao.contador_id == numero_vacinacao:
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