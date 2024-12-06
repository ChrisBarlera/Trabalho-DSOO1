from DAOs.DAO_abstract import DAO
from entidade.Adotante import Adotante

class AdotanteDAO(DAO):
    def __init__(self):
        super().__init__('adotante.pkl')

    def add(self, adotante: Adotante):
        if (isinstance(adotante.cpf, int)) and (adotante is not None) \
            and (isinstance(adotante, Adotante)):
            super().add(adotante.cpf, adotante)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)