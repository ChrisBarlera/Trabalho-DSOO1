class TelaAnimal:
    def tela_opcoes(self):
        print("\n-------- ANIMAL ----------")
        print("Escolha a opcao")
        print("1 - Incluir Animal")
        print("2 - Alterar Animal")
        print("3 - Listar Animais")
        print("4 - Excluir Animal")
        print("0 - Retornar")
        
        opcao = int(input("Escolha a opcao: "))
        return opcao
    
    def pega_dados_animal(self):
        tipo = self.decide_tipo_animal()
        print("\n-------- DADOS ANIMAL ----------")
        numero_chip = int(input("Número do chip: "))
        nome = input("Nome: ")
        raca = input("Raça: ")

        if tipo == 2: # Tipo Cachorro
            tamanho = input("Tamanho: ")
            return {"numero_chip": numero_chip, "nome": nome, "raca": raca, "tamanho":tamanho}
        else:
            return {"numero_chip": numero_chip, "nome": nome, "raca": raca}
    
    def decide_tipo_animal(self):
        print("\n-------- TIPO ANIMAL ----------")
        print("Escolha a opcao")
        print("1 - Gato")
        print("2 - Cachorro")

        opcao = int(input("Escolha a opcao: "))
        return opcao
    
    def mostra_animal(self, dados_animal):
        print("TITULO DO animal: ", dados_animal["titulo"])
        print("CODIGO DO animal: ", dados_animal["codigo"])
        print("\n")