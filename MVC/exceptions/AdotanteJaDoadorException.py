class AdotanteJaDoadorException(Exception):
    def __init__(self):
        self.mensagem = 'Esta pessoa não pode adotar (já doou antes)'
        super().__init__(self.mensagem)
