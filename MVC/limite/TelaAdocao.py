from datetime import date as Date

class TelaAdocao:
    def tela_opcoes(self):
        print('\n-------- ADOÇÃO ----------')
        print('1 - Incluir Adoção')
        print('2 - Alterar Adoção')
        print('3 - Listar Adoções')
        print('4 - Excluir Adoção')
        print('0 - Retornar')
        
        opcao = int(input('Escolha a opção: '))
        return opcao
    
    def pega_dados_adocao(self):
        print('\n-------- DADOS ADOÇÃO ----------')
        raw_data_nasc = input('Data da Adoção (Formato dd/mm/yyyy): ').split('/')
        data_dict = {'day': int(raw_data_nasc[0]),
                     'month': int(raw_data_nasc[1]),
                     'year': int(raw_data_nasc[2])}
        data = Date(**data_dict)
        return {'data': data}
    
    def mostra_adocao(self, dados_adocao):
        print('\nDATA DA ADOÇÃO: ', dados_adocao['data'])

    def seleciona_adocao(self):
        numero = int(input('\nNúmero da adoção que deseja selecionar: '))
        return numero

    def ja_tem_adotante(self):
        resposta = bool(int(input('\nAdotante já cadastrado? (1: Sim, 0: Não): ')))
        return resposta
    
    def ja_tem_animal(self):
        resposta = bool(int(input('\nAnimal já cadastrado? (1: Sim, 0: Não): ')))
        return resposta
    
    def mostra_mensagem(self, msg):
        print(f'\n{msg}')