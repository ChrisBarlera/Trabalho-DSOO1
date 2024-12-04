from DAOs.DAO_abstract import DAO
from entidade.Habitacao import Habitacao

class HabitacaoDAO(DAO):
    def __init__(self):
        super().__init__('habitacao.pkl')

    def add(self, habitacao: Habitacao):
        if (isinstance(habitacao.numero_chip, int)) and (habitacao is not None) \
            and (isinstance(habitacao, Habitacao)):
            super().add(habitacao.numero_chip, habitacao)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)