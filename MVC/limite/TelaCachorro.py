import PySimpleGUI as sg


class TelaCachorro:
    def tela_opcoes(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Cachorro',size=(20,1), font=titulo)],
            [
                sg.Button('Incluir', size=20, font=botao_font),
                sg.Button('Alterar', size=20, font=botao_font),
                sg.Button('Listar', size=20, font=botao_font),
                sg.Button('Excluir', size=20, font=botao_font)
            ],
            [sg.Button('Retornar', size=20, font=botao_font)]
        ]
        self.__window = sg.Window('Sistema da ONG', default_element_size=(200,1)).Layout(layout)
        
        retorno, values = self.open()
        dicionario = {
            'Incluir' : 1,
            'Alterar' : 2,
            'Listar' : 3,
            'Excluir' : 4,
            'Retornar' : 0
        }
        self.close()
        return dicionario[retorno]
    
    def pega_dados_cachorro(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Insira os dados',size=(20,1), font=titulo)],
            [sg.Text('Número do chip', size=20, font=botao_font),
             sg.Input('Ex.: 123', size=20, font=('Helvetica', 15), key='numero_chip')],
            [sg.Text('Nome do animal', size=20, font=botao_font),
             sg.Input('Ex.: Fulaninho', size=20, font=('Helvetica', 15), key='nome')],
            [sg.Text('Raça', size=20, font=botao_font),
             sg.Input('Ex.: Uma Raça', size=20, font=('Helvetica', 15), key='raca')],
            [sg.Text('Tamanho/Porte', size=20, font=botao_font), sg.Combo((
                'Pequeno',
                'Médio',
                'Grande'
            ), font=('Helvetica', 15), size=20, readonly=True, key='tamanho')],
            [sg.Ok(size=20, font=botao_font)]
        ]
        self.__window = sg.Window('Sistema da ONG', default_element_size=(200,1)).Layout(layout)
        button, values = self.open()

        try:
            values['numero_chip'] = int(values['numero_chip'])
            if values['tamanho'] == '':
                raise ValueError
        except ValueError:
            self.mostra_mensagem('Preenchimento inválido dos dados!')
            self.close()
            self.pega_dados_cachorro()


        return values
    
    def seleciona_cachorro(self):
        numero = int(input('\nNúmero do cachorro para selecionar: '))
        return numero
    
    def mostra_cachorro(self, dados_cachorro):
        mapa_de_tamanhos = {
            1: 'Pequeno',
            2: 'Médio',
            3: 'Grande'
        }
        print('\nNÚMERO DO CACHORRO: ', dados_cachorro['numero_chip'])
        print('NOME DO CACHORRO: ', dados_cachorro['nome'])
        print('RACA DO CACHORRO: ', dados_cachorro['raca'])
        print('TAMANHO DO CACHORRO: ', mapa_de_tamanhos[dados_cachorro['tamanho']])

    def mostra_mensagem(self, mensagem: str, titulo='Mensagem'):
        sg.Popup(titulo, mensagem)

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()