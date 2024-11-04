from datetime import date as Date
from entidade.Pessoa import Pessoa
from entidade.Habitacao import Habitacao


class Adotante(Pessoa):
    def __init__(self, cpf: int, nome: str, data_nasc: Date, endereco: str,
                 habitacao: Habitacao, possui_animais: bool):
        super().__init__(cpf, nome, data_nasc, endereco)
        self.__habitacao = None
        self.__possui_animais = None

        ### Testando tipos das variáveis
        if isinstance(habitacao, Habitacao):
            self.__habitacao = habitacao
        else:
            print('Tipo inválido')
        
        if isinstance(possui_animais, bool):
            self.__possui_animais = possui_animais
        else:
            print('Tipo inválido')

    @property
    def habitacao(self):
        return self.__habitacao
    
    @habitacao.setter
    def habitacao(self, habitacao: Habitacao):
        if isinstance(habitacao, Habitacao):
            self.__habitacao = habitacao
        else:
            print('Valor inválido. O valor deve ser um Habitacao')
    
    @property
    def possui_animais(self):
        return self.possui_animais
    
    @possui_animais.setter
    def possui_animais(self, possui_animais: bool):
        if isinstance(possui_animais, bool):
            self.possui_animais = possui_animais
        else:
            print('Valor inválido. O valor deve ser um bool')

    def calcula_idade(self):
        hoje = Date.today()
        return (hoje - self.__data_nasc).days // 365 # type: ignore
