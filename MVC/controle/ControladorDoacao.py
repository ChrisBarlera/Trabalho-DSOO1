from limite.TelaDoacao import TelaDoacao
from entidade.Doacao import Doacao
from controle.ControladorDoador import ControladorDoador
from DAOs.DoacaoDAO import DoacaoDAO


class ControladorDoacao:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_doador = controlador_sistema.controlador_doador
        self.__controlador_animal = controlador_sistema.controlador_animal
        self.__doacoes = [] # type: ignore
        self.__tela_doacao = TelaDoacao()
        self.__contador_id = 1
        self.__doacao_DAO = DoacaoDAO()
        try:
            self.__doacoes = list(self.__doacao_DAO.get_all())
        except:
            pass

    def incluir_doacao(self):
        adotante = None
        animal = None
        
        if self.ja_tem_doador():
            cpf = self.__controlador_doador.lista_doadores(seleciona=True)
            doador = self.__controlador_doador.pega_doador_por_cpf(cpf)
        else:
            self.__tela_doacao.mostra_mensagem('Cadastre um doador')
            doador = self.__controlador_doador.incluir_doador()
        
        if self.ja_tem_animal():
            numero = self.__controlador_animal.lista_animais(seleciona=True)
            animal = self.__controlador_animal.pega_animal_por_numero(numero)
        else:
            self.__tela_doacao.mostra_mensagem('Cadastre um animal')
            animal = self.__controlador_animal.incluir_animal()
        
        dados_doacao = self.__tela_doacao.pega_dados_doacao()
        nova_doacao = Doacao(self.__contador_id, doador, animal,
                             dados_doacao['data'], dados_doacao['motivo'])
        self.__contador_id += 1
        self.__doacoes.append(nova_doacao)
        return nova_doacao
    
    def alterar_doacao(self):
        self.lista_doacoes()
        numero_doacao = self.__tela_doacao.seleciona_doacao()
        doacao = self.pega_doacao_por_numero(numero_doacao)

        if doacao is not None:
            if self.tbm_trocar_doador():
                self.__tela_doacao.mostra_mensagem('Cadastre o doador')
                novo_doador = self.__controlador_doador.incluir_doador()
                doacao.doador = novo_doador

            if self.tbm_trocar_animal():
                self.__tela_doacao.mostra_mensagem('Cadastre o animal')
                novo_animal = self.__controlador_animal.incluir_animal()
                doacao.animal = novo_animal
            novos_dados = self.__tela_doacao.pega_dados_doacao()
            doacao.data = novos_dados['data']
        else:
            self.__tela_doacao.mostra_mensagem('ATENCAO: adoção não existente')
        self.lista_doacoes()
        return doacao

    def lista_doacoes(self):
        for doacao in self.__doacoes:
            dados = {'numero_id': doacao.numero_id,
                     'data': doacao.data,
                     'animal': doacao.animal,
                     'doador': doacao.doador}
            self.__tela_doacao.mostra_doacao(dados)
            self.__controlador_animal.mostra_animal_especifico(dados['animal'])
            self.__controlador_doador.mostra_doador_especifico(dados['doador'])

    def excluir_doacao(self):
        self.lista_doacoes()
        numero_doacao = self.__tela_doacao.seleciona_doacao()
        doacao = self.pega_doacao_por_numero(numero_doacao)

        if doacao is not None:
            self.__doacoes.remove(doacao)
        else:
            self.__tela_doacao.mostra_mensagem('ATENCAO: doação não existente')
        
        self.lista_doacoes()

    def pega_doacao_por_numero(self, numero_id):
        for doacao in self.__doacoes:
            if doacao.numero_id == numero_id:
                return doacao
        return None
    
    def pessoa_ja_doou(self, cpf_busca):
        for doacao in self.__doacoes:
            if doacao.doador.cpf == cpf_busca:
                return True
        return False

    def ja_tem_doador(self):
        return self.__tela_doacao.ja_tem_doador()
    
    def ja_tem_animal(self):
        return self.__tela_doacao.ja_tem_animal()

    def tbm_trocar_doador(self):
        return self.__tela_doacao.tbm_trocar_doador()
    
    def tbm_trocar_animal(self):
        return self.__tela_doacao.tbm_trocar_animal()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_doacao,
                        2: self.alterar_doacao,
                        3: self.lista_doacoes,
                        4: self.excluir_doacao,
                        0: self.retornar}

        while True:
            lista_opcoes[self.__tela_doacao.tela_opcoes()]()
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()