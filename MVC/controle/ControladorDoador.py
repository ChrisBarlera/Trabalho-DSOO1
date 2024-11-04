from limite.TelaDoador import TelaDoador
from entidade.Doador import Doador


class ControladorDoador:

    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__doadores = [] # type: ignore
        self.__tela_doador = TelaDoador()

    def incluir_doador(self):
        dados_doador = self.__tela_doador.pega_dados_doador()
        novo_doador = Doador(dados_doador['cpf'], 
                         dados_doador['nome'],
                         dados_doador['data_nasc'],
                         dados_doador['endereco'])
        self.__doadores.append(novo_doador)
        return novo_doador
    
    def alterar_doador(self):
        self.lista_doadores()
        numero_doador = self.__tela_doador.seleciona_doador()
        doador = self.pega_doador_por_cpf(numero_doador)

        if doador is not None:
            novos_dados = self.__tela_doador.pega_dados_doador()
            doador.cpf = novos_dados['cpf']
            doador.nome = novos_dados['nome']
            doador.data_nasc = novos_dados['data_nasc']
            doador.endereco = novos_dados['endereco']
        else:
            self.__tela_doador.mostra_mensagem('ATENCAO: doador não existente')
        self.lista_doadores()

    def lista_doadores(self):
        for doador in self.__doadores:
            dados = {'cpf': doador.cpf,
                     'nome': doador.nome,
                     'data_nasc': doador.data_nasc,
                     'endereco': doador.endereco}
            self.__tela_doador.mostra_doador(dados)

    def excluir_doador(self):
        self.lista_doadores()
        numero_doador = self.__tela_doador.seleciona_doador()
        doador = self.pega_doador_por_cpf(numero_doador)

        if doador is not None:
            self.__doadores.remove(doador)
        else:
            self.__tela_doador.mostra_mensagem('ATENCAO: doador não existente')
        
        self.lista_doadores()

    def pega_doador_por_cpf(self, cpf_doador):
        for doador in self.__doadores:
            if doador.cpf == cpf_doador:
                return doador
        return None
    
    def seleciona_doador(self):
        self.lista_doadores()
        cpf = self.__tela_doador.seleciona_doador()
        return self.pega_doador_por_cpf(cpf)
    
    def mostra_doador_especifico(self, doador):
        dados = {'nome': doador.nome,
                 'cpf': doador.cpf}
        self.__tela_doador.mostra_doador_especifico(dados)

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_doador,
                        2: self.alterar_doador,
                        3: self.lista_doador,
                        4: self.excluir_doador,
                        0: self.retornar}

        while True:
            lista_opcoes[self.__tela_doador.tela_opcoes()]()
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()