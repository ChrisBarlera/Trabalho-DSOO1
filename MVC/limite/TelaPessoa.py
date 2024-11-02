from datetime import date as Date


class TelaPessoa:
    def tela_opcoes(self):
        print('\n-------- PESSOA ----------')
        print('1 - Incluir Pessoa')
        print('2 - Alterar Pessoa')
        print('3 - Listar Pessoas')
        print('4 - Excluir Pessoa')
        print('0 - Retornar')
        
        opcao = int(input('Escolha a opção: '))
        return opcao
    
    def pega_dados_pessoa(self):
        tipo = self.decide_tipo_pessoa()
        print('\n-------- DADOS PESSOA ----------')
        cpf = input('CPF: ')
        nome = input('Nome: ')
        raw_data_nasc = input('Data de Nascimento (Formato, dd/mm/aaaa): ').split('/')
        data_dict = {'day': int(raw_data_nasc[0]),
                     'month': int(raw_data_nasc[1]),
                     'year': int(raw_data_nasc[2])}
        data_nasc = Date(**data_dict)
        endereco = input('Endereco: ')
        
        if tipo == 1: # Tipo Doador
            return {
                'cpf': cpf, 'nome': nome,
                'data_nasc': data_nasc, 'endereco': endereco
            }
        else:
            # return {
            #     'cpf': cpf, 'nome': nome,
            #     'data_nasc': data_nasc, 'endereco': endereco,
            #     'habitacao': habitacao
            # }
            pass

    def decide_tipo_pessoa(self):
        print('\n-------- TIPO PESSOA ----------')
        print('1 - Doador')
        print('2 - Adotante')

        opcao = int(input('Escolha a opção: '))
        return opcao

    def decide_mostra_tipo(self):
        print('\n-------- TIPO PESSOA ----------')
        print('Temos as seguintes listas:')
        print('1 - Doador')
        print('2 - Adotante')
        print('3 - Todos')

        opcao = int(input('Escolha a opção: '))
        return opcao
