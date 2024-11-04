from datetime import date as Date

class TelaDoacao:
    def tela_opcoes(self):
        print('\n-------- DOAÇÃO ----------')
        print('1 - Incluir Doação')
        print('2 - Alterar Doação')
        print('3 - Listar Doações')
        print('4 - Excluir Doação')
        print('0 - Retornar')
        
        opcao = int(input('Escolha a opção: '))
        return opcao
    
    def pega_dados_doacao(self):
        print('\n-------- DADOS DOAÇÃO ----------')
        raw_data_nasc = input('Data da Doação (Formato dd/mm/yyyy): ').split('/')
        data_dict = {'day': int(raw_data_nasc[0]),
                     'month': int(raw_data_nasc[1]),
                     'year': int(raw_data_nasc[2])}
        data = Date(**data_dict)
        motivo = input('Motivo da doação: ')
        return {'data': data, 'motivo': motivo}
    
    def mostra_doacao(self, dados_doacao):
        print('\nID DA DOAÇÃO: ', dados_doacao['numero_id'])
        print('DATA DA DOAÇÃO: ', dados_doacao['data'])

    def seleciona_doacao(self):
        numero = int(input('\nID da doação que deseja selecionar: '))
        return numero

    def ja_tem_doador(self):
        resposta = bool(int(input('\nDoador já cadastrado? (1: Sim, 0: Não): ')))
        return resposta
    
    def ja_tem_animal(self):
        resposta = bool(int(input('\nAnimal já cadastrado? (1: Sim, 0: Não): ')))
        return resposta
    
    def tbm_trocar_doador(self):
        resposta = bool(int(input('\nTambém alterar doador? (1: Sim, 0: Não): ')))
        return resposta
    
    def tbm_trocar_animal(self):
        resposta = bool(int(input('\nTambém alterar animal? (1: Sim, 0: Não): ')))
        return resposta
    
    def mostra_mensagem(self, msg):
        print(f'\n{msg}')