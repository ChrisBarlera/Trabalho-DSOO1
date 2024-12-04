from DAOs.DAO_abstract import DAO
from entidade.Gato import Gato

class GatoDAO(DAO):
    def __init__(self):
        super().__init__('gato.pkl')

    def add(self, gato: Gato):
        if (isinstance(gato.numero_chip, int)) and (gato is not None) \
            and (isinstance(gato, Gato)):
            super().add(gato.numero_chip, gato)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)