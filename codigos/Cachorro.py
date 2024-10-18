from Animal import Animal


class Cachorro(Animal):
    def __init__(self, numero_chip: int, nome: str, raca: str, tamanho: str):
        super().__init__(numero_chip, nome, raca)
        self.__tamanho = None

        if isinstance(tamanho, str):
            self.__tamanho = tamanho
        else:
            print('Tipo inválido')