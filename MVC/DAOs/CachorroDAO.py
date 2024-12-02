from DAOs.DAO_abstract import DAO
from entidade.Cachorro import Cachorro

class CachorroDAO(DAO):
    def __init__(self):
        super().__init__('cachorro.pkl')

    def add(self, cachorro: Cachorro):
        if (isinstance(cachorro.numero_chip, int)) and (cachorro is not None) \
            and (isinstance(cachorro, Cachorro)):
            super().add(cachorro.numero_chip, cachorro)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)