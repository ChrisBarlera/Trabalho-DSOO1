from entidade.Pessoa import Pessoa
from datetime import date as Date


class Doador(Pessoa):
    def __init__(self, cpf: int, nome: str, data_nasc: Date, endereco: str):
        super().__init__(cpf, nome, data_nasc, endereco)