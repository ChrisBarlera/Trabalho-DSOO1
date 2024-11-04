from datetime import date as Date


class TelaAdotante:
    def tela_opcoes(self):
        print('\n-------- ADOTANTE ----------')
        print('1 - Incluir Adotante')
        print('2 - Alterar Adotante')
        print('3 - Listar Adotantes')
        print('4 - Excluir Adotante')
        print('0 - Retornar')
        
        opcao = int(input('Escolha a opção: '))
        return opcao
    
    def pega_dados_adotante(self):
        print('\n-------- DADOS ADOTANTE ----------')
        cpf = int(input('CPF: '))
        nome = input('Nome: ')
        raw_data_nasc = input('Data de Nascimento (Formato dd/mm/2024): ').split('/')
        data_dict = {'day': int(raw_data_nasc[0]),
                     'month': int(raw_data_nasc[1]),
                     'year': int(raw_data_nasc[2])}
        data_nasc = Date(**data_dict)
        endereco = input('Seu endereço completo: ')
        possui_animais = bool(int(input('Possui animais? (1: Sim, 0: Não): ')))

        return {'cpf': cpf, 'nome': nome,
                'data_nasc': data_nasc, 'endereco': endereco,
                'possui_animais': possui_animais}
    
    def mostra_adotante(self, dados_adotante):
        print('\nCPF DO ADOTANTE: ', dados_adotante['cpf'])
        print('NOME DO ADOTANTE: ', dados_adotante['nome'])
        print('DATA DE NASCIMENTO DO ADOTANTE: ', dados_adotante['data_nasc'])
        print('ENDEREÇO DO ADOTANTE: ', dados_adotante['endereco'])
        print('ADOTANTE POSSUI ANIMAIS?: ', dados_adotante['possui_animais'])

    def seleciona_adotante(self):
        cpf = int(input('\nCPF do adotante para selecionar: '))
        return cpf
    
    def mostra_mensagem(self, msg):
        print(msg)