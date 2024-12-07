from DAOs.DAO_abstract import DAO
from entidade.Adocao import Adocao

class AdocaoDAO(DAO):
    def __init__(self):
        super().__init__('adocao.pkl')

    def add(self, adocao: Adocao):
        if (isinstance(adocao.numero_id, int)) and (adocao is not None) \
            and (isinstance(adocao, Adocao)):
            super().add(adocao.numero_id, adocao)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)