from limite.TelaAdocao import TelaAdocao
from entidade.Adocao import Adocao


class ControladorAdocao:
    def __init__(self, controlador_sistema, controlador_adotante, controlador_animal):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_adotante = controlador_adotante
        self.__controlador_animal = controlador_animal
        self.__adocoes = [] # type: ignore
        self.__tela_adocao = TelaAdocao()

    def incluir_adocao(self):
        self.__controlador_animal.lista_animais()
        self.__controlador_adotante.lista_adotantes()
        numero_adocao = self.__tela_adocao.seleciona_adocao()
        adocao = self.pega_adocao_por_numero(numero_adocao)

        dados_adocao = self.__tela_adocao.pega_dados_adocao()
        nova_adocao = Adocao(dados_adocao['cpf'], 
                         dados_adocao['nome'],
                         dados_adocao['data_nasc'],
                         dados_adocao['endereco'])
        self.__adocoes.append(nova_adocao)
        return nova_adocao
    
    def alterar_adocao(self):
        self.lista_adocoes()
        numero_adocao = self.__tela_adocao.seleciona_adocao()
        adocao = self.pega_adocao_por_numero(numero_adocao)

        if adocao is not None:
            novos_dados = self.__tela_adocao.pega_dados_adocao()
            adocao.cpf = novos_dados['cpf']
            adocao.nome = novos_dados['nome']
            adocao.data_nasc = novos_dados['data_nasc']
            adocao.endereco = novos_dados['endereco']
        else:
            self.__tela_adocao.mostra_mensagem('ATENCAO: adoção não existente')
        self.lista_adocoes()

    def lista_adocoes(self):
        for adocao in self.__adocoes:
            dados = {'cpf': adocao.cpf,
                     'nome': adocao.nome,
                     'data_nasc': adocao.data_nasc,
                     'endereco': adocao.endereco}
            self.__tela_adocao.mostra_adocao(dados)

    def excluir_adocao(self):
        self.lista_adocoes()
        numero_adocao = self.__tela_adocao.seleciona_adocao()
        adocao = self.pega_adocao_por_numero(numero_adocao)

        if adocao is not None:
            self.__adocoes.remove(adocao)
        else:
            self.__tela_adocao.mostra_mensagem('ATENCAO: adoção não existente')
        
        self.lista_adocoes()

    def pega_adocao_por_numero(self, numero_doacao):
        for adocao in self.__adocoes:
            if adocao.cpf == numero_doacao:
                return adocao
        return None

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_adocao,
                        2: self.alterar_adocao,
                        3: self.lista_adocao,
                        4: self.excluir_adocao,
                        0: self.retornar}

        while True:
            lista_opcoes[self.__tela_adocao.tela_opcoes()]()
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()