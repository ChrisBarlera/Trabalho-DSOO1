class MenorDeIdadeException(Exception):
    def __init__(self):
        self.mensagem = 'Esta pessoa não pode adotar (é menor de idade)'
        super().__init__(self.mensagem)
