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
        print('\n-------- DADOS DOAÇÃO ----------')
        
        # cpf = int(input('CPF: '))
        # nome = input('Nome: ')
        # raw_data_nasc = input('Data de Nascimento (Formato dd/mm/2024): ').split('/')
        # data_dict = {'day': int(raw_data_nasc[0]),
        #              'month': int(raw_data_nasc[1]),
        #              'year': int(raw_data_nasc[2])}
        # data_nasc = Date(**data_dict)
        # endereco = input('Seu endereço completo: ')

        # return {'cpf': cpf, 'nome': nome,
        #         'data_nasc': data_nasc, 'endereco': endereco}
    
    def mostra_adocao(self, dados_adocao):
        print('\nCPF DO ADOÇÃO: ', dados_adocao['cpf'])
        print('NOME DO ADOÇÃO: ', dados_adocao['nome'])
        print('DATA DE NASCIMENTO DO ADOÇÃO: ', dados_adocao['data_nasc'])
        print('ENDEREÇO DO ADOÇÃO: ', dados_adocao['endereco'])

    def seleciona_adocao(self):
        numero = int(input('\nNúmero da adoção que deseja selecionar: '))
        return numero
    
    def mostra_mensagem(self, msg):
        print(msg)