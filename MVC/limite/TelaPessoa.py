class Telapessoa:
    def tela_opcoes(self):
        print("\n-------- PESSOA ----------")
        print("1 - Incluir Pessoa")
        print("2 - Alterar Pessoa")
        print("3 - Listar Pessoas")
        print("4 - Excluir Pessoa")
        print("0 - Retornar")
        
        opcao = int(input("Escolha a opção: "))
        return opcao
    
    def pega_dados_pessoa(self):
        tipo = self.decide_tipo_pessoa()
        print("\n-------- DADOS PESSOA ----------")
        numero_chip = int(input("Número do chip: "))
        nome = input("Nome: ")
        raca = input("Raça: ")

        if tipo == 2: # Tipo Cachorro
            tamanho = input("Tamanho: ")
            return {"numero_chip": numero_chip, "nome": nome, "raca": raca, "tamanho":tamanho}
        else:
            return {"numero_chip": numero_chip, "nome": nome, "raca": raca}
    
    def decide_tipo_pessoa(self):
        print("\n-------- TIPO PESSOA ----------")
        print("1 - Gato")
        print("2 - Cachorro")

        opcao = int(input("Escolha a opção: "))
        return opcao
    
    def mostra_pessoa(self, dados_pessoa):
        print("TITULO DO pessoa: ", dados_pessoa["titulo"])
        print("CODIGO DO pessoa: ", dados_pessoa["codigo"])
        print("\n")

    def decide_mostra_tipo(self):
        print("\n-------- TIPO PESSOA ----------")
        print("Temos as seguintes listas:")
        print("1 - Gato")
        print("2 - Cachorro")
        print("3 - Todos")

        opcao = int(input("Escolha a opção: "))
        return opcao
