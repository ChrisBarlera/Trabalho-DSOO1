from datetime import date as Date


class TelaVacinacao:
    def tela_opcoes(self):
        print('\n-------- VACINAÇÃO ----------')
        print('1 - Incluir Vacinação')
        print('2 - Alterar Vacinação')
        print('3 - Listar Vacinações')
        print('4 - Excluir Vacinação')
        print('0 - Retornar')
        
        opcao = int(input('Escolha a opção: '))
        return opcao
    
    def pega_dados_vacinacao(self):
        print('\n-------- DADOS VACINAÇÃO ----------')
        raw_data_nasc = input('Data da Vacinação (Formato dd/mm/yyyy): ').split('/')
        data_dict = {'day': int(raw_data_nasc[0]),
                     'month': int(raw_data_nasc[1]),
                     'year': int(raw_data_nasc[2])}
        data = Date(**data_dict)
        vacina = input('Nome da vacina: ')
        return {'data': data, 'vacina': vacina}
    
    def mostra_vacinacao(self, dados_vacinacao):
        print('\nNÚMERO DA VACINAÇÃO: ', dados_vacinacao['numero'])
        print('NOME DA VACINAÇÃO: ', dados_vacinacao['tipo'])
        print('TAMANHO DA VACINAÇÃO: ', dados_vacinacao['tamanho'])

    def seleciona_vacinacao(self):
        numero = int(input('\nNúmero da vacinação para selecionar: '))
        return numero
    
    def mostra_mensagem(self, msg):
        print(f'\n{msg}')