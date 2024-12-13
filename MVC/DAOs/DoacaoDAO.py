from DAOs.DAO_abstract import DAO
from entidade.Doacao import Doacao

class DoacaoDAO(DAO):
    def __init__(self):
        super().__init__('doacao.pkl')

    def add(self, doacao: Doacao):
        if (isinstance(doacao.numero_id, int)) and (doacao is not None) \
            and (isinstance(doacao, Doacao)):
            super().add(doacao.numero_id, doacao)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)