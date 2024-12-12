from limite.TelaVacinacao import TelaVacinacao
from entidade.Vacinacao import Vacinacao
from DAOs.VacinacaoDAO import VacinacaoDAO


class ControladorVacinacao:

    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__controlador_animal = controlador_sistema.controlador_animal
        self.__vacinacoes = [] # type: ignore
        self.__tela_vacinacao = TelaVacinacao()
        self.__vacinacao_DAO = VacinacaoDAO()
        self.init_DAO()

    def init_DAO(self):
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
        nova_vacinacao = Vacinacao(dados_vacinacao['codigo'],
                                   dados_vacinacao['data'],
                                   dados_vacinacao['vacina'])
        self.__vacinacoes.append(nova_vacinacao)
        animal.vacinacoes.append(nova_vacinacao)
        self.__vacinacao_DAO.add(nova_vacinacao)
        self.__controlador_animal.update_vacinacao(animal)
        return nova_vacinacao
    
    def alterar_vacinacao(self):
        pass

    def lista_vacinacoes(self, selecionar=False):
        numero = self.__controlador_animal.lista_animais(True)
        animal = self.__controlador_animal.pega_animal_por_numero(numero)
        lista_dados = []
        for vacinacao in animal.vacinacoes:
            dados = {'codigo': vacinacao.codigo,
                     'data': vacinacao.data,
                     'nome_animal': animal.nome,
                     'vacina': vacinacao.vacina}
            lista_dados.append(dados)
        return self.__tela_vacinacao.mostra_todas_vacinacoes(
            lista_dados,
            selecionar
        ), animal

    def excluir_vacinacao(self):
        codigo, animal = self.lista_vacinacoes(selecionar=True)
        vacinacao = self.pega_vacinacao_por_codigo(codigo)
        self.__vacinacao_DAO.remove(vacinacao.codigo)
        self.__vacinacoes.remove(vacinacao)
        animal.remover_vacina_por_codigo(codigo)
        self.__controlador_animal.update_vacinacao(animal)
        self.init_DAO()
        return vacinacao

    def pega_vacinacao_por_codigo(self, codigo_vacinacao):
        for vacinacao in self.__vacinacoes:
            if vacinacao.codigo == codigo_vacinacao:
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