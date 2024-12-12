from datetime import date as Date
import PySimpleGUI as sg


class TelaVacinacao:

    def __init__(self) -> None:
        self.__window = None

    def tela_opcoes(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Vacinação',size=(20,1), font=titulo)],
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
    
    def pega_dados_vacinacao(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Insira os dados',size=(20,1), font=titulo)],
            [sg.Text('Data de vacina (Formato dd/mm/yyyy)', size=20, font=botao_font),
             sg.Input('Ex.: 13/12/2024', size=20, font=('Helvetica', 15), key='data')],
            [sg.Text('Vacina', size=20, font=botao_font), sg.Combo((
                'Raiva',
                'Leptospirose',
                'Hepatite Infecciosa'
            ), font=('Helvetica', 15), size=20, readonly=True, key='vacina')],
            [sg.Ok(size=20, font=botao_font)]
        ]
        self.__window = sg.Window('Sistema da ONG', default_element_size=(200,1)).Layout(layout)
        button, values = self.open()
        try:
            raw_data = values['data'].split('/')
            data_dict = {'day': int(raw_data[0]),
                     'month': int(raw_data[1]),
                     'year': int(raw_data[2])}
            values['data'] = Date(**data_dict)
            if values['vacina'] == '':
                raise ValueError
        except:
            self.mostra_mensagem('Preenchimento inválido dos dados!')
            self.close()
            self.pega_dados_vacinacao()
        self.close()
        return values

    def mostra_todas_vacinacoes(self, lista):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [[sg.Text('Vacinacoes cadastrados',size=(20,1), font=titulo)]]

        for vacinacao in lista:
            layout.append(self.mostra_vacinacao(vacinacao))
            layout.append([sg.Text('-------------------------------------------')])
        self.__window = sg.Window('Sistema da ONG', default_element_size=(200,1)).Layout(layout)
        retorno, values = self.open()
        self.close()
        return retorno
    
    def mostra_vacinacao(self, dados_vacinacao):
        vac_layout = [
            [sg.Text(f'Número: {dados_vacinacao['contador_id']}')],
            [sg.Text(f'Vacina: {dados_vacinacao['vacina']}')],
            [sg.Text(f'Data: {dados_vacinacao['data']}')],
            [sg.Text(f'Animal: {dados_vacinacao['nome_animal']}')]
        ]
        return vac_layout

    def ja_tem_animal(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Animal já cadastrado?',size=(20,1), font=titulo)],
            [
                sg.Button('Sim', size=20, font=botao_font),
                sg.Button('Não', size=20, font=botao_font)
            ]
        ]
        self.__window = sg.Window('Sistema da ONG', default_element_size=(200,1)).Layout(layout)
        retorno, values = self.open()
        dicionario = {
            'Sim' : True,
            'Não' : False
        }
        self.close()
        return dicionario[retorno]

    def mostra_mensagem(self, mensagem: str, titulo='Mensagem'):
        sg.Popup(titulo, mensagem)

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()