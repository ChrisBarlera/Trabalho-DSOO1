from limite.TelaAdotante import TelaAdotante
from entidade.Adotante import Adotante


class ControladorAdotante:
    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__adotantes = [] # type: ignore
        self.__tela_adotante = TelaAdotante()

    def incluir_adotante(self):
        dados_adotante = self.__tela_adotante.pega_dados_adotante()
        novo_adotante = Adotante(dados_adotante['cpf'], 
                         dados_adotante['nome'],
                         dados_adotante['data_nasc'],
                         dados_adotante['endereco'],
                         '', # Precisa ver habitacao
                         dados_adotante['possui_animais'])
        self.__adotantes.append(novo_adotante)
        return novo_adotante
    
    def alterar_adotante(self):
        self.lista_adotantes()
        numero_adotante = self.__tela_adotante.seleciona_adotante()
        adotante = self.pega_adotante_por_cpf(numero_adotante)

        if adotante is not None:
            novos_dados = self.__tela_adotante.pega_dados_adotante()
            adotante.cpf = novos_dados['cpf']
            adotante.nome = novos_dados['nome']
            adotante.data_nasc = novos_dados['data_nasc']
            adotante.endereco = novos_dados['endereco']
            adotante.habitacao = novos_dados['habitacao']
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
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()