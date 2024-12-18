from limite.TelaAnimal import TelaAnimal
from DAOs.CachorroDAO import CachorroDAO
from DAOs.GatoDAO import GatoDAO

class ControladorAnimal:

    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__controlador_gato = controlador_sistema.controlador_gato
        self.__controlador_cachorro = controlador_sistema.controlador_cachorro
        # self.__controlador_vacinacao = controlador_sistema.controlador_vacinacao
        self.__animais = [] # type: ignore # E se eu fizer uma matriz Nx2?
        self.__tela_animal = TelaAnimal()
        self.__cachorro_DAO = CachorroDAO()
        self.__gato_DAO = GatoDAO()
        self.init_DAO()
        
    def init_DAO(self):
        try:
            self.__animais = list(self.__cachorro_DAO.get_all())
            for gato in list(self.__gato_DAO.get_all()):
                self.__animais.append(gato)
        except:
            pass
    
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

    def lista_animais(self, seleciona=False):
        lista_dados = []
        for animal in self.__animais:
            try:
                dados = {
                    'nome': animal.nome,
                    'numero_chip': animal.numero_chip,
                    'especie': animal.especie,
                    'tamanho': animal.tamanho
                }
            except:
                dados = {
                    'nome': animal.nome,
                    'numero_chip': animal.numero_chip,
                    'especie': animal.especie
                }
            lista_dados.append(dados)
        return self.__tela_animal.mostra_todos_animais(lista_dados, seleciona)

    def excluir_animal(self):
        opcao = self.__tela_animal.decide_tipo_animal()
        if opcao == 1:
            self.__controlador_gato.excluir_gato()
        else:
            self.__controlador_cachorro.excluir_cachorro()
        self.init_DAO()

    def pega_animal_por_numero(self, numero_animal):
        for animal in self.__animais:
            if animal.numero_chip == numero_animal:
                return animal
        return None

    def mostra_animal_especifico(self, animal):
        dados = {'nome': animal.nome,
                 'numero': animal.numero_chip,
                 'especie': animal.especie,
                 'raca': animal.raca}
        self.__tela_animal.mostra_animal_especifico(dados)

    def tem_todas_vacinas(self, animal):
        feitas = set()
        for vacinacao in animal.vacinacoes:
            if vacinacao.vacina not in feitas:
                feitas.add(vacinacao.vacina)
        
        if len(feitas) == 3:
            return True
        else:
            return False

    def update_vacinacao(self, animal):
        if animal.especie == 'Cachorro':
            self.__cachorro_DAO.remove(animal.numero_chip)
            self.__cachorro_DAO.add(animal)
            # self.__cachorro_DAO.update(animal.numero_chip, animal)
        else:
            self.__gato_DAO.remove(animal.numero_chip)
            self.__gato_DAO.add(animal)
            # self.__gato_DAO.update(animal.codigo,animal)
        self.init_DAO()

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

    @property
    def animais(self):
        return self.__animais