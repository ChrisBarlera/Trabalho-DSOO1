import PySimpleGUI as sg


class TelaHabitacao:

    def __init__(self) -> None:
        self.__window = None

    def tela_opcoes(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Habitação',size=(20,1), font=titulo)],
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
    
    def pega_dados_habitacao(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Insira os dados',size=(20,1), font=titulo)],
            [sg.Text('Número da habitação', size=20, font=botao_font),
             sg.Input('Ex.: 123', size=20, font=('Helvetica', 15), key='numero')],
            [sg.Text('Tipo', size=20, font=botao_font), sg.Combo((
                'Casa',
                'Apartamento'
            ), font=('Helvetica', 15), size=20, readonly=True, key='tipo')],
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
            values['numero'] = int(values['numero'])
            if values['tipo'] == '' or values['tamanho'] == '':
                raise ValueError
        except ValueError:
            self.mostra_mensagem('Preenchimento inválido dos dados!')
            self.close()
            self.pega_dados_habitacao()
        self.close()
        return values
    
    def mostra_habitacao(self, dados_habitacao):
        hab_layout = [
            [sg.Text(f'Número: {dados_habitacao['numero']}')],
            [sg.Text(f'Tipo: {dados_habitacao['tipo']}')],
            [sg.Text(f'Tamanho: {dados_habitacao['tamanho']}')]
        ]
        return hab_layout

    def mostra_todas_habitacoes(self, lista, selecionar=False):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [[sg.Text('Habitações cadastradas',size=(20,1), font=titulo)]]
        if selecionar:
            for habitacao in lista:
                layout.append(self.mostra_habitacao(habitacao))
                layout.append([sg.Button(f'Selecionar {habitacao['numero']}')])
                layout.append([sg.Text('-------------------------------------------')])
        else:
            for habitacao in lista:
                layout.append(self.mostra_habitacao(habitacao))
                layout.append([sg.Text('-------------------------------------------')])
        self.__window = sg.Window('Sistema da ONG', default_element_size=(200,1)).Layout(layout)
        retorno, values = self.open()
        if selecionar:
            retorno = int(retorno[11::])
        self.close()
        return retorno
    
    def mostra_mensagem(self, mensagem: str, titulo='Mensagem'):
        sg.Popup(titulo, mensagem)

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()