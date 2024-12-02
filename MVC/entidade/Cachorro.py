from entidade.Animal import Animal


class Cachorro(Animal):
    def __init__(self, numero_chip: int, nome: str, raca: str, tamanho: int):
        super().__init__(numero_chip, nome, raca)
        self.__tamanho = tamanho
        
        self.__especie = 'Cachorro'

    @property
    def especie(self):
        return self.__especie
    
    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, tamanho: str):
        if isinstance(tamanho, str):
            self.__tamanho = tamanho
        else:
            print('Valor inválido. O valor deve ser um str')
