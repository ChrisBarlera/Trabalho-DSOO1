class TelaAnimal:
    def tela_opcoes(self):
        print("\n-------- ANIMAL ----------")
        print("1 - Incluir Animal")
        print("2 - Alterar Animal")
        print("3 - Listar Animais")
        print("4 - Excluir Animal")
        print("0 - Retornar")
        
        opcao = int(input("Escolha a opção: "))
        return opcao
    
    def pega_dados_animal(self):
        tipo = self.decide_tipo_animal()
        print("\n-------- DADOS ANIMAL ----------")
        numero_chip = int(input("Número do chip: "))
        nome = input("Nome: ")
        raca = input("Raça: ")

        if tipo == 2: # Tipo Cachorro
            tamanho = input("Tamanho: ")
            return {"numero_chip": numero_chip,
                    "nome": nome, "raca": raca, "tamanho": tamanho}
        else:
            return {"numero_chip": numero_chip, "nome": nome, "raca": raca}
    
    def decide_tipo_animal(self):
        print("\n-------- TIPO ANIMAL ----------")
        print("1 - Gato")
        print("2 - Cachorro")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def decide_mostra_tipo(self):
        print("\n-------- TIPO ANIMAL ----------")
        print("Temos as seguintes listas:")
        print("1 - Gato")
        print("2 - Cachorro")
        print("3 - Todos")

        opcao = int(input("Escolha a opção: "))
        return opcao
