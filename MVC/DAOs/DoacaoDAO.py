from DAOs.DAO_abstract import DAO
from entidade.Doacao import Doacao

class DoacaoDAO(DAO):
    def __init__(self):
        super().__init__('doacao.pkl')

    def add(self, daocao: Doacao):
        if (isinstance(daocao.numero_id, int)) and (daocao is not None) \
            and (isinstance(daocao, daocao)):
            super().add(daocao.numero_id, daocao)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)