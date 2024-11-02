class TelaGato:
    def tela_opcoes(self):
        print("\n-------- GATO ----------")
        print("1 - Incluir gato")
        print("2 - Alterar gato")
        print("3 - Listar Animais")
        print("4 - Excluir gato")
        print("0 - Retornar")
        
        opcao = int(input("Escolha a opção: "))
        return opcao
    
    def pega_dados_gato(self):
        print("\n-------- DADOS GATO ----------")
        numero_chip = int(input("Número do chip: "))
        nome = input("Nome: ")
        raca = input("Raça: ")

        return {"numero_chip": numero_chip, "nome": nome, "raca": raca}
    
    def mostra_gato(self, dados_gato):
        print("\nNUMERO DO GATO: ", dados_gato["numero_chip"])
        print("NOME DO GATO: ", dados_gato["nome"])
        print("RACA DO GATO: ", dados_gato["raca"])

    def seleciona_gato(self):
        numero = int(input("\nNumero do gato que deseja selecionar: "))
        return numero
    
    def mostra_mensagem(self, msg):
        print(msg)