class FaltaDeEspacoException(Exception):
    def __init__(self):
        self.mensagem = 'Cão grande demais para o apartamento'
        super().__init__(self.mensagem)
