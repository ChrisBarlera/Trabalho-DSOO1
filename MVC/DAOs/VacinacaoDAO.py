from DAOs.DAO_abstract import DAO
from entidade.Vacinacao import Vacinacao

class VacinacaoDAO(DAO):
    def __init__(self):
        super().__init__('vacinacao.pkl')

    def add(self, vacinacao: Vacinacao):
        if (isinstance(vacinacao.contador_id, int)) and (vacinacao is not None) \
            and (isinstance(vacinacao, Vacinacao)):
            super().add(vacinacao.contador_id, vacinacao)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)