from datetime import date as Date

class TelaDoador:
    def tela_opcoes(self):
        print('\n-------- DAODOR ----------')
        print('1 - Incluir Doador')
        print('2 - Alterar Doador')
        print('3 - Listar Doadores')
        print('4 - Excluir Doador')
        print('0 - Retornar')
        
        opcao = int(input('Escolha a opção: '))
        return opcao
    
    def pega_dados_doador(self):
        print('\n-------- DADOS DOADOR ----------')
        cpf = int(input('CPF: '))
        nome = input('Nome: ')
        raw_data_nasc = input('Data de Nascimento (Formato dd/mm/2024): ').split('/')
        data_dict = {'day': int(raw_data_nasc[0]),
                     'month': int(raw_data_nasc[1]),
                     'year': int(raw_data_nasc[2])}
        data_nasc = Date(**data_dict)
        endereco = input('Seu endereço completo: ')

        return {'cpf': cpf, 'nome': nome,
                'data_nasc': data_nasc, 'endereco': endereco}
    
    def mostra_doador(self, dados_doador):
        print('\nCPF DO DOADOR: ', dados_doador['cpf'])
        print('NOME DO DOADOR: ', dados_doador['nome'])
        print('DATA DE NASCIMENTO DO DOADOR: ', dados_doador['data_nasc'])
        print('ENDEREÇO DO DOADOR: ', dados_doador['endereco'])

    def seleciona_doador(self):
        numero = int(input('\nCPF do doador que deseja selecionar: '))
        return numero
    
    def mostra_doador_especifico(self, dados_doador):
        print('NOME DO DOADOR:', dados_doador['nome'])
        print('CPF DO DOADOR:', dados_doador['cpf'])

    def mostra_mensagem(self, msg):
        print(msg)