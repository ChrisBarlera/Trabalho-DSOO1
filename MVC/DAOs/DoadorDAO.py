from DAOs.DAO_abstract import DAO
from entidade.Doador import Doador

class DoadorDAO(DAO):
    def __init__(self):
        super().__init__('doador.pkl')

    def add(self, doador: Doador):
        if (isinstance(doador.numero_chip, int)) and (doador is not None) \
            and (isinstance(doador, Doador)):
            super().add(doador.numero_chip, doador)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)