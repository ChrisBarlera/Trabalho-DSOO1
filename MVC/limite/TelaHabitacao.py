class TelaHabitacao:
    def tela_opcoes(self):
        print('\n-------- HABITAÇÃO ----------')
        print('1 - Incluir Habitação')
        print('2 - Alterar Habitação')
        print('3 - Listar Habitações')
        print('4 - Excluir Habitação')
        print('0 - Retornar')
        
        opcao = int(input('Escolha a opção: '))
        return opcao
    
    def pega_dados_habitacao(self):
        print('\n-------- DADOS HABITAÇÃO ----------')
        numero = int(input('Número: '))
        print('Tipo 1: Casa')
        print('Tipo 2: Apartamento')
        tipo = int(input('Escolha um tipo: '))
        print('Tamanho 1: Pequeno')
        print('Tamanho 2: Médio')
        print('Tamanho 3: Grande')
        tamanho = int(input('Escolha um tamanho: '))

        return {'numero': numero, 'tipo': tipo, 'tamanho': tamanho}
    
    def mostra_habitacao(self, dados_habitacao):
        mapa_tamanhos = {
            1: 'Pequeno',
            2: 'Médio',
            3: 'Grande',
        }
        mapa_tipos = {
            1: 'Casa',
            2: 'Apartamento'
        }
        print('\nNÚMERO DA HABITAÇÃO: ', dados_habitacao['numero'])
        print('TIPO DA HABITAÇÃO: ', mapa_tipos[dados_habitacao['tipo']])
        print('TAMANHO DA HABITAÇÃO: ', mapa_tamanhos[dados_habitacao['tamanho']])

    def seleciona_habitacao(self):
        numero = int(input('\nNúmero da habitação para selecionar: '))
        return numero
    
    def mostra_mensagem(self, msg):
        print(msg)