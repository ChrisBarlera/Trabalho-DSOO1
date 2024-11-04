class TelaCachorro:
    def tela_opcoes(self):
        print('\n-------- CACHORRO ----------')
        print('1 - Incluir cachorro')
        print('2 - Alterar cachorro')
        print('3 - Listar cachorros')
        print('4 - Excluir cachorro')
        print('0 - Retornar')
        
        opcao = int(input('Escolha a opção: '))
        return opcao
    
    def pega_dados_cachorro(self):
        print('\n-------- DADOS CACHORRO ----------')
        numero_chip = int(input('Número do chip: '))
        nome = input('Nome: ')
        raca = input('Raça: ')
        tamanho = input('Tamanho: ')

        return {'numero_chip': numero_chip, 'nome': nome,
                'raca': raca, 'tamanho': tamanho}
    
    def seleciona_cachorro(self):
        numero = int(input('\nNúmero do cachorro para selecionar: '))
        return numero
    
    def mostra_cachorro(self, dados_cachorro):
        print('\nNÚMERO DO CACHORRO: ', dados_cachorro['numero_chip'])
        print('NOME DO CACHORRO: ', dados_cachorro['nome'])
        print('RACA DO CACHORRO: ', dados_cachorro['raca'])
        print('TAMANHO DO CACHORRO: ', dados_cachorro['tamanho'])