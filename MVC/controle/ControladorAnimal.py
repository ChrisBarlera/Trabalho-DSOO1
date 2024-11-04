from limite.TelaAnimal import TelaAnimal


class ControladorAnimal:

    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__controlador_gato = controlador_sistema.controlador_gato
        self.__controlador_cachorro = controlador_sistema.controlador_cachorro
        self.__animais = [] # type: ignore # E se eu fizer uma matriz Nx2?
        self.__tela_animal = TelaAnimal()

    def incluir_animal(self):
        opcao = self.__tela_animal.decide_tipo_animal()
        if opcao == 1:
            novo_animal = self.__controlador_gato.incluir_gato()
        else:
            novo_animal = self.__controlador_cachorro.incluir_cachorro()
        self.__animais.append(novo_animal)
        return novo_animal
    
    def alterar_animal(self):
        opcao = self.__tela_animal.decide_tipo_animal()
        if opcao == 1:
            self.__controlador_gato.alterar_gato()
        else:
            self.__controlador_cachorro.alterar_cachorro()

    def lista_animais(self):
        opcao = self.__tela_animal.decide_mostra_tipo()

        if opcao == 1:
            self.__controlador_gato.lista_gatos() # placeholder
        elif opcao == 2:
            self.__controlador_cachorro.lista_cachorros()
        else:
            # for animal in self.__animais:
            #     if isinstance(animal,Gato):
            #         self.__controlador_gato.lista_gatos()
            print(self.__animais) # placeholder
        

    def excluir_animal(self):
        opcao = self.__tela_animal.decide_tipo_animal()
        if opcao == 1:
            self.__controlador_gato.excluir_gato()
        else:
            self.__controlador_cachorro.excluir_cachorro()

    def seleciona_animal(self):
        opcao = self.__tela_animal.decide_tipo_animal()
        if opcao == 1:
            animal = self.__controlador_gato.seleciona_gato()
        else:
            animal = self.__controlador_cachorro.seleciona_cachorro()
        return animal

    def mostra_animal_especifico(self, animal):
        dados = {'nome': animal.nome,
                 'numero': animal.numero_chip,
                 'especie': animal.especie,
                 'raca': animal.raca}
        self.__tela_animal.mostra_animal_especifico(dados)

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_animal,
                        2: self.alterar_animal,
                        3: self.lista_animais,
                        4: self.excluir_animal,
                        0: self.retornar}

        while True:
            lista_opcoes[self.__tela_animal.tela_opcoes()]()
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()
