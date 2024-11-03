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
