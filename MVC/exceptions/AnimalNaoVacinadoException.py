class AnimalNaoVacinadoException(Exception):
    def __init__(self):
        self.mensagem = 'Só podem ser adotados animais vacinados'
        super().__init__(self.mensagem)
