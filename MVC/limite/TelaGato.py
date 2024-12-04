import PySimpleGUI as sg


class TelaGato:

    def __init__(self) -> None:
        self.__window = None

    def tela_opcoes(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Gato',size=(20,1), font=titulo)],
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
    
    def pega_dados_gato(self):
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
            [sg.Ok(size=20, font=botao_font)]
        ]
        self.__window = sg.Window('Sistema da ONG', default_element_size=(200,1)).Layout(layout)
        button, values = self.open()

        try:
            values['numero_chip'] = int(values['numero_chip'])
        except:
            self.mostra_mensagem('Preenchimento inválido dos dados!')
            self.close()
            self.pega_dados_gato()
        self.close()
        return values
    
    def mostra_todos_gatos(self, lista, selecionar=False):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [[sg.Text('Gatos cadastrados',size=(20,1), font=titulo)]]
        if selecionar:
            for gato in lista:
                layout.append(self.mostra_gato(gato))
                layout.append([sg.Button(f'Selecionar {gato['numero_chip']}')])
                layout.append([sg.Text('-------------------------------------------')])
        else:
            for gato in lista:
                layout.append(self.mostra_gato(gato))
                layout.append([sg.Text('-------------------------------------------')])
        self.__window = sg.Window('Sistema da ONG', default_element_size=(200,1)).Layout(layout)
        retorno, values = self.open()
        if selecionar:
            retorno = int(retorno[11::])
        self.close()
        return retorno

    def mostra_gato(self, dados_gato):
        cat_layout = [
            [sg.Text(f'Número: {dados_gato['numero_chip']}')],
            [sg.Text(f'Nome: {dados_gato['nome']}')],
            [sg.Text(f'Raça: {dados_gato['raca']}')]
        ]
        return cat_layout
    
    def mostra_mensagem(self, mensagem: str, titulo='Mensagem'):
        sg.Popup(titulo, mensagem)

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()