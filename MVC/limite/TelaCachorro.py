class TelaCachorro:
    def tela_opcoes(self):
        print("\n-------- CACHORRO ----------")
        print("1 - Incluir cachorro")
        print("2 - Alterar cachorro")
        print("3 - Listar cachorros")
        print("4 - Excluir cachorro")
        print("0 - Retornar")
        
        opcao = int(input("Escolha a opção: "))
        return opcao
    
    def pega_dados_cachorro(self):
        print("\n-------- DADOS CACHORRO ----------")
        numero_chip = int(input("Número do chip: "))
        nome = input("Nome: ")
        raca = input("Raça: ")
        tamanho = input("Tamanho: ") # Tem que ver isso aí

        return {"numero_chip": numero_chip, "nome": nome,
                "raca": raca, "tamanho": tamanho}
    
    # def mostra_cachorro(self, dados_cachorro):
    #     print("TITULO DO CACHORRO: ", dados_cachorro["titulo"])
    #     print("CODIGO DO CACHORRO: ", dados_cachorro["codigo"])
    #     print("\n")