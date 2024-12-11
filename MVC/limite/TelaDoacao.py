import PySimpleGUI as sg
from datetime import date as Date

class TelaDoacao:
    def tela_opcoes(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Doações',size=(20,1), font=titulo)],
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
    
    def pega_dados_doacao(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Insira os dados',size=(20,1), font=titulo)],
            [sg.Text('Data da doação (Formato dd/mm/yyyy)', size=20, font=botao_font),
             sg.Input('Ex.: 13/12/2024', size=20, font=('Helvetica', 15), key='data')],
            [sg.Text('Motivo da doação', size=20, font=botao_font),
             sg.Input('Ex.: Sem espaço em casa', size=20, font=('Helvetica', 15), key='motivo')],
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
        except:
            self.mostra_mensagem('Preenchimento inválido dos dados!')
            self.close()
            self.pega_dados_doacao()
        self.close()
        return values
    
    def mostra_doacao(self, dados_doacao):
        print('\nID DA DOAÇÃO: ', dados_doacao['numero_id'])
        print('DATA DA DOAÇÃO: ', dados_doacao['data'])

    def seleciona_doacao(self):
        numero = int(input('\nID da doação que deseja selecionar: '))
        return numero

    def ja_tem_doador(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Doador já cadastrado?',size=(20,1), font=titulo)],
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
    
    def tbm_trocar_doador(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Também alterar doador?',size=(20,1), font=titulo)],
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
    
    def tbm_trocar_animal(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Também alterar animal?',size=(20,1), font=titulo)],
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
