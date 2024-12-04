import PySimpleGUI as sg


class TelaCachorro:

    def __init__(self) -> None:
        self.__window = None
        sg.ChangeLookAndFeel('DarkGreen2')

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
        self.close()
        return values
    
    def mostra_todos_cachorros(self, lista, selecionar=False):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [[sg.Text('Cachorros cadastrados',size=(20,1), font=titulo)]]
        if selecionar:
            for cachorro in lista:
                layout.append(self.mostra_cachorro(cachorro))
                layout.append([sg.Button(f'Selecionar {cachorro['numero_chip']}')])
                layout.append([sg.Text('-------------------------------------------')])
        else:
            for cachorro in lista:
                layout.append(self.mostra_cachorro(cachorro))
                layout.append([sg.Text('-------------------------------------------')])
        self.__window = sg.Window('Sistema da ONG', default_element_size=(200,1)).Layout(layout)
        retorno, values = self.open()
        if selecionar:
            retorno = int(retorno[11::])
        self.close()
        return retorno

    def mostra_cachorro(self, dados_cachorro):
        dog_layout = [
            [sg.Text(f'Número: {dados_cachorro['numero_chip']}')],
            [sg.Text(f'Nome: {dados_cachorro['nome']}')],
            [sg.Text(f'Raça: {dados_cachorro['raca']}')],
            [sg.Text(f'Tamanho: {dados_cachorro['tamanho']}')]
        ]
        return dog_layout

    def mostra_mensagem(self, mensagem: str, titulo='Mensagem'):
        sg.Popup(titulo, mensagem)

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()