from limite.TelaAdotante import TelaAdotante
from entidade.Adotante import Adotante
from controle.ControladorHabitacao import ControladorHabitacao


class ControladorAdotante:
    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__controlador_habitacao = controlador_sistema.controlador_habitacao
        self.__adotantes = [] # type: ignore
        self.__tela_adotante = TelaAdotante()

    def incluir_adotante(self):
        habitacao = None
        if self.habitacao_ja_cadastrada():
            self.__controlador_habitacao.lista_habitacoes()
            numero = self.__controlador_habitacao.__tela_habitacao.seleciona_habitacao()
            habitacao = self.__controlador_habitacao.pega_habitacao_por_numero(numero)
        else:
            self.__tela_adotante.mostra_mensagem('Cadastre uma habitação')
            habitacao = self.__controlador_habitacao.incluir_habitacao()

        self.__tela_adotante.mostra_mensagem('Cadastre o adotante')
        dados_adotante = self.__tela_adotante.pega_dados_adotante()
        novo_adotante = Adotante(dados_adotante['cpf'], 
                        dados_adotante['nome'],
                        dados_adotante['data_nasc'],
                        dados_adotante['endereco'],
                        habitacao,
                        dados_adotante['possui_animais'])
        self.__adotantes.append(novo_adotante)
        return novo_adotante

    def alterar_adotante(self):
        self.lista_adotantes()
        numero_adotante = self.__tela_adotante.seleciona_adotante()
        adotante = self.pega_adotante_por_cpf(numero_adotante)

        if adotante is not None:
            if self.tbm_trocar_habitacao():
                nova_hab = self.__controlador_habitacao.incluir_habitacao()
                adotante.habitacao = nova_hab
            novos_dados = self.__tela_adotante.pega_dados_adotante()
            adotante.cpf = novos_dados['cpf']
            adotante.nome = novos_dados['nome']
            adotante.data_nasc = novos_dados['data_nasc']
            adotante.endereco = novos_dados['endereco']
            adotante.possui_animais = novos_dados['possui_animais']
        else:
            self.__tela_adotante.mostra_mensagem('ATENCAO: adotante não existente')
        self.lista_adotantes()

    def lista_adotantes(self):
        for adotante in self.__adotantes:
            dados = {'cpf': adotante.cpf,
                     'nome': adotante.nome,
                     'data_nasc': adotante.data_nasc,
                     'endereco': adotante.endereco,
                     'habitacao': adotante.habitacao,
                     'possui_animais': adotante.possui_animais}
            self.__tela_adotante.mostra_adotante(dados)

    def excluir_adotante(self):
        self.lista_adotantes()
        numero_adotante = self.__tela_adotante.seleciona_adotante()
        adotante = self.pega_adotante_por_cpf(numero_adotante)

        if adotante is not None:
            self.__adotantes.remove(adotante)
        else:
            self.__tela_adotante.mostra_mensagem('ATENCAO: adotante não existente')
        
        self.lista_adotantes()

    def pega_adotante_por_cpf(self, cpf_adotante):
        for adotante in self.__adotantes:
            if adotante.cpf == cpf_adotante:
                return adotante
        return None

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_adotante,
                        2: self.alterar_adotante,
                        3: self.lista_adotante,
                        4: self.excluir_adotante,
                        0: self.retornar}

        while True:
            lista_opcoes[self.__tela_adotante.tela_opcoes()]()

    def seleciona_adotante(self):
        self.lista_adotantes()
        cpf = self.__tela_adotante.seleciona_adotante()
        return self.pega_adotante_por_cpf(cpf)
    
    def mostra_adotante_especifico(self, adotante):
        dados = {'nome': adotante.nome,
                 'cpf': adotante.cpf}
        self.__tela_adotante.mostra_adotante_especifico(dados)

    def habitacao_ja_cadastrada(self):
        return self.__tela_adotante.habitacao_ja_cadastrada()
    
    def tbm_trocar_habitacao(self):
        return self.__tela_adotante.tbm_trocar_habitacao()
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()
