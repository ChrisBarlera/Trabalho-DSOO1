class TelaAnimal:
    def tela_opcoes(self):
        print("-------- ANIMAL ----------")
        print("Escolha a opcao")
        print("1 - Incluir Animal")
        print("2 - Alterar Animal")
        print("3 - Listar Animais")
        print("4 - Excluir Animal")
        print("0 - Retornar")
        
        opcao = int(input("Escolha a opcao: "))
        return opcao
    
    def pega_dados_animal(self):
        print("-------- DADOS ANIMAL ----------")
        numero_chip = int(input("Número do chip: "))
        nome = input("Nome: ")
        raca = input("Raça: ")

        return {"numero_chip": numero_chip, "nome": nome, "raca": raca}
    
    def mostra_animal(self, dados_animal):
        print("TITULO DO animal: ", dados_animal["titulo"])
        print("CODIGO DO animal: ", dados_animal["codigo"])
        print("\n")